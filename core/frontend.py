import re
from time import time, sleep

import allure

from exceptions import FailStep


class __Base:
    wait = lambda s, x: sleep(x)

    def __init__(self, browser):
        self._browser = browser


class Authorization(__Base):
    @allure.step('Autorization to the Application as {1} successful')
    def login(self, login, passwd):
        el = self._browser.get_by_id('Username')
        el.send_keys(login)
        self._browser.get_by_id('Password').send_keys(passwd)
        self._browser.get_by_id('btnLogin').click()
        time_start = time()

        while self._browser.get_by_id('btnLogin', need_fail=False, custom_time_out=1):
            if time() - time_start > 10:
                raise FailStep('not authorization after 10s')

    @allure.step('Correct Deautorization from Application')
    def logout(self):
        pass


class Steps(__Base):
    spaces = re.compile(r'\s+')

    @allure.step('Click on {1} button verification ')
    def click_button(self, name, text=False):
        if not text:
            el = self._browser.get_by_id(name)
        else:
            el = self._browser.get_by_xpath(f'//*[contains(text(), "{name}")]')
        self._browser.scroll(el)
        el.click()

    @allure.step('Verify modal dialog {1}')
    def click_button_on_modal_dialog(self, name):
        self._browser.get_by_xpath(f'//div[contains(@class, "modal")]//button[contains(text(), "{name}")]').click()

    @allure.step('Verify Drop-Down Field {1} is presented')
    def click_on_dropdown(self, name):
        self._browser.get_by_xpath(f'//div[@class="DropdownLabel"]//p[contains(text(), "{name}")]').click()

    @allure.step('Select Product {1} / verify {1} is presented')
    def choose_in_dropdown(self, name):
        self._browser.get_by_xpath(f'//div[@class="DropdownLabel"]//option[contains(text(), "{name}")]').click()

    @allure.step('Go to {1}/ element is presented')
    def goto(self, name):
        self._browser.get_by_id(name).click()

    @allure.step('Go to {1} verify element')
    def navigate(self, name):
        el = self._browser.get_by_xpath(f'//div[@class="Component"]//*[contains(text(), "{name}")]')
        self._browser.scroll(el)
        el.click()

    @allure.step('Select {1} table tab and verify')
    def choose_tab(self, name):
        self._browser.get_by_xpath(f'//table[@class="table-tabs"]//a[contains(text(), "{name}")]').click()

    @allure.step('Select {1} checkbox / verify ')
    def choose_checkbox(self, name, test=False):
        t = '' if test else '//ul[@class="radioButtonTypeWizard"]'
        self._browser.get_by_xpath(f'{t}//*[contains(text(), "{name}")]').click()


    @allure.step('Select value {1} from_table verify')
    def choose_on_table(self, name):
        self._browser.get_by_xpath(f'//table//td[contains(text(), "{name}")]', is_elements_list=True,
                                   need_fail=False).click()

    @allure.step('Fill table {1} and verify ')
    def fill_table(self, table, type_='textarea'):
        for key, value in table.items():
            el = self._browser.get_by_xpath(f'''//{type_}[contains(@name, "{self.spaces.sub('', key)}")]''')
            el.send_keys(value)

    @allure.step('Select/verify {1}')
    def choose_on_dropdown_in_table(self, name, value, _id=None):
        xpath = f'''//select[contains(@name, "{self.spaces.sub('', name)}")]'''
        if _id:
            xpath = f'//select[id={_id}]'
        self._browser.get_by_xpath(xpath).click()
        self._browser.get_by_xpath(f'{xpath}//option[contains(text(), "{value}")]').click()

    @allure.step('Set checkbox {1} verify')
    def set_checkbox_in_table(self, name, value):
        el = self._browser.get_by_xpath(f'''//*[@type="checkbox" and contains(@name, "{self.spaces.sub('', name)}")]''')

        if value != el.value:
            el.click()

    @allure.step('Choose Author {1} verify selection')
    def choose_authors(self, name, authors_list):
        xpath = f'''//select[contains(@name , "{self.spaces.sub('', name)}")]/option[contains(text(), "%s")]'''
        for v in authors_list:
            self._browser.get_by_xpath(xpath % v).click()
            self._browser.get_by_id('jq-moveAuthorsAdd').click()

    @allure.step ('Task validation')
    def config_task(self, task, config):
        task_id = "divTaskID_%s" % self._browser.get_by_xpath(
            f'//td[@class="table-tasks-sequence" and contains(text(), "{task}")]').get_attribute('title')
        xpath = '//tr[@id="%s"]//td//span[contains(text(), "%s")]/../..//input[contains(@id, "%s")]'
        self._browser.get_by_id('img_%s' % task_id).click()
        for k, v in config.items():
            el = self._browser.get_by_xpath(xpath % (task_id, k, v))
            self._browser.scroll(el)
            el.click()

    @allure.step('Setup filter {1}/verify element is present')
    def set_filter(self, name, value):
        xpath = f'//th//a[contains(text(), "{name}")]/../'
        el = self._browser.get_by_xpath('%s/*[@data-action="filter-trigger"]' % xpath)
        self._browser.scroll(el)
        sleep(.5)
        el.click()
        self._browser.get_by_id(value).click()
        self._browser.get_by_xpath('%s/*[@data-action="filter-submit"]' % xpath).click()

    @allure.step('Get value {1} verify')
    def get_values_on_table(self, index):
        elements = self._browser.get_by_xpath(f'//tbody//td[{index}]', is_elements_list=True)
        return [el.text for el in elements]

    @allure.step('Click element and verified')
    def click_element_by_tag(self, tag):
        self._browser.get_by_tag(tag).click()

    @allure.step('Select element and verified')
    def click_element_by_tag(self, name):
        self._browser.get_by_name(name).click()