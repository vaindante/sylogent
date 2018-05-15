import os
from json import dumps

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, \
    NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from exceptions import SeleniumWebDriverError, SeleniumBrowserNotStarting
from logger import logger


class ReconnectForDriver:
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            for attempt in range(2, -1, -1):
                try:
                    try:
                        instance.close_all_popups()
                    except NoAlertPresentException:
                        pass

                    self.method(instance, *args, **kwargs)
                    break

                except Exception as e:
                    # return instance
                    instance.status = 'restart'
                    logger.warning('Произошла ошибка c браузером %s' % instance.node_info, exc_info=e)
                    if instance.node_connect_retry_count:
                        instance.node_connect_retry_count -= 1
                        instance.restart_session()

            else:
                logger.fatal('Все плохо, прям совсем %s' % instance)
                raise SeleniumBrowserNotStarting()

        return wrapper


class SeleniumWebDriver:
    # Get selenium driver
    # Информация о использованных ссесиях
    session_info = []
    # Информация о текущих окнах
    window = {}
    cookies = None
    status = None

    def __init__(self, **kwargs):
        self.driver = None
        self.time_out = int(os.getenv('SELENIUM_TIMEOUT', 15))

        self.node_info = None
        self.node_connect_retry_count = int(os.getenv('SELENIUM_COUNT_RESTART_BROWSER', 10))

        self.__dict__.update(kwargs)
        self.start_session()

    def __str__(self):
        return dumps(
            {
                'session_info': self.session_info,
                'count_restart_node': self.node_connect_retry_count,
                'status': self.status
            },
            indent=4)

    def __prepare_window(self, url):
        self.delete_all_cookies()
        self.open_url(url)

    def start_session(self):
        # Пытаемся подключиться к selenium ноде (делаем 3 попытки)
        logger.info('Selenium: create new object driver(browser)')
        capabilities = {
            "browserName": "chrome",
            "version": "61.0",
        }
        if os.getenv('USE_LOCALHOST', None) or getattr(self, 'local', None):
            self.driver = webdriver.Chrome(
                os.getenv('CHROME_DRIVER_PATH', './core/chromedriver'),
            )

        else:
            self.driver = webdriver.Remote(
                command_executor=os.getenv('SELENIUM_HUB', 'http://selenium:selenium@sg.yandex-team.ru:4444/wd/hub'),
                desired_capabilities=capabilities
            )

        # Подменяем класс, если мы хотим работать со своим классом, то и получать должны его
        # self.driver._web_element_cls = SeleniumWebElement

        # Set selenium driver parameters
        self.driver.set_script_timeout(15)

        # Get diagnostic info from selenium node and put it to STDOUT
        self.node_info = {
            'session_id': self.driver.session_id,
            'failed': False
        }

        self.status = 'started'
        self.window.update({'window': self.driver.window_handles[0]})
        self.session_info.append(self.node_info)
        logger.info('Session: %s' % self)

    # Полная перезагрузка браузера с создание нового объекта и новых окон
    def restart_session(self):
        self.start_session()
        self.open_url(self.window['url'])

    def get_cookies(self):
        self.cookies = {v['name']: v['value'] for v in self.driver.get_cookies()}

    # Сброс кэша и перезагрузка страница для автономности тестов
    @ReconnectForDriver
    def reload(self):
        self.status = 'clean'
        if self.status == 'started':
            logger.subdebug('Очистка окна %r с url %r' % (self.window['window'], self.window['url']))
            self.driver.switch_to_window(self.window['window'])
            self.driver.execute_script('window.localStorage.clear(); location.reload();')
            self.__prepare_window(self.window['url'])

        self.status = 'started'

    def logs(self):
        exclude_logs = [
        ]
        return [
            item['message'] for item in self.driver.get_log('browser')
            if any([log not in item['message'] for log in exclude_logs])
        ]

    # Selenium tools ###################################################################################################
    def save_screenshot(self, save_path):
        # Get screenshot
        self.driver.save_screenshot(save_path)

    @ReconnectForDriver
    def delete_all_cookies(self):
        # Clear browser cookie
        self.driver.delete_all_cookies()

    def quit(self):
        # Close browser session
        self.driver.quit()

    @ReconnectForDriver
    def open_url(self, url):
        # Got to URL
        logger.debug('Open url: %s' % url)
        self.driver.get(url)

    @property
    def current_url(self):
        # Get current url
        return self.driver.current_url

    @property
    def url(self):
        return self.window['url']

    @property
    def yandexuid(self):
        return self.cookies['yandexuid']

    # Elements getters #################################################################################################
    def get_element(self, path_type, element_path, need_fail=True, custom_time_out=None, is_elements_list=False):
        """
        Get element
                :param path_type: тип локатора
                :param element_path: путь элемента
                :param need_fail:
                :param custom_time_out:
                :param is_elements_list:
                :return:
        """

        __type = {
            'xpath': By.XPATH,
            'css': By.CSS_SELECTOR,
            'id': By.ID,
            'class': By.CLASS_NAME
        }
        if custom_time_out is not None:
            time_out = custom_time_out
        else:
            time_out = self.time_out

        try:
            if not is_elements_list:
                # Очень нужная, вещь, так как при ошибки с элементом, мы понятия не имеем, какой элемент мы запросили.
                logger.debug('Получение элемента тип %r путь %r' % (path_type, element_path))
                return WebDriverWait(self.driver, time_out).until(
                    expected_conditions.presence_of_element_located((__type.get(path_type), element_path))
                )
            else:
                logger.debug('Получение списка элементов тип %r путь %r' % (path_type, element_path))
                return WebDriverWait(self.driver, time_out).until(
                    expected_conditions.presence_of_all_elements_located((__type.get(path_type), element_path))
                )

        except (TimeoutException, UnexpectedAlertPresentException):
            if need_fail:
                raise SeleniumWebDriverError('Cannot find element by %s: %r' % (path_type, element_path))
            else:
                if is_elements_list:
                    return list()
                else:
                    return need_fail

    def get_by_xpath(self, xpath, need_fail=True, is_elements_list=False, custom_time_out=None):
        # Get element by XPath
        return self.get_element('xpath', xpath, need_fail=need_fail, is_elements_list=is_elements_list,
                                custom_time_out=custom_time_out)

    def get_by_css(self, css, need_fail=True, is_elements_list=False, custom_time_out=None):
        # Get element by CSS
        return self.get_element('css', css, need_fail=need_fail, is_elements_list=is_elements_list,
                                custom_time_out=custom_time_out)

    def get_by_id(self, e_id, need_fail=True, is_elements_list=False, custom_time_out=None):
        # Get element by ID
        return self.get_element('id', e_id, need_fail=need_fail, is_elements_list=is_elements_list,
                                custom_time_out=custom_time_out)

    def close_all_popups(self):
        # Закрытие iframe
        alert = self.driver.switch_to.alert
        if alert is not None:
            alert.accept()
