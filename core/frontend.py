from time import time

import allure

from exceptions import FailStep


class __Base:
    def __init__(self, browser):
        self._browser = browser


class Authorization(__Base):
    @allure.step('Авторизуемся на сайте под логином {1}')
    def login(self, login, passwd):
        el = self._browser.get_by_id('Username')
        el.send_keys(login)
        self._browser.get_by_id('Password').send_keys(passwd)
        self._browser.get_by_id('btnLogin').click()
        time_start = time()

        while self._browser.get_by_id('btnLogin', need_fail=False, custom_time_out=1):
            if time() - time_start > 10:
                raise FailStep('not authorization after 10s')

    @allure.step('Деавторизуемся')
    def logout(self):
        pass


class Steps(__Base):
    @allure.step('Click on button {1}')
    def click_button(self, name):
        self._browser.get_by_id(name).click()

    def click_button_on_modal_dialog(self, name):
        self._browser.get_by_xpath(f'//div[contains(@class, "modal")]//button[contains(text(), "{name}")]').click()

    @allure.step('Расскрываем список {1}')
    def click_on_dropdown(self, name):
        self._browser.get_by_xpath(f'//div[@class="DropdownLabel"]//p[contains(text(), "{name}")]').click()

    @allure.step('Выбираем {1}')
    def choose_in_dropdown(self, name):
        self._browser.get_by_xpath(f'//div[@class="DropdownLabel"]//option[contains(text(), "{name}")]').click()

    @allure.step('Go to {1}')
    def goto(self, name):
        self._browser.get_by_id(name).click()

    def navigate(self, name):
        el = self._browser.get_by_xpath(f'//ul[@class="navigation"]//a[contains(text(), "{name}")]')
        el.click()

    def choose_tab(self, name):
        self._browser.get_by_xpath(f'//table[@class="table-tabs"]//a[contains(text(), "{name}")]').click()

    def choose_checkbox(self, name, test=False):
        t = '' if test else '//ul[@class="radioButtonTypeWizard"]'
        self._browser.get_by_xpath(f'{t}//*[contains(text(), "{name}")]').click()

    def choose_on_table(self, name):
        self._browser.get_by_xpath(f'//table//td[contains(text(), "{name}")]').click()

    # дальше шаги будут описывать по мере необходимости
