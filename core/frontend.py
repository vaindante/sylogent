import allure


class __Base:
    def __init__(self, browser):
        self._browser = browser


class Authorization(__Base):
    @allure.step('Авторизуемся на сайте под логином {1}')
    def login(self, login, passwd):
        pass

    @allure.step('Деавторизуемся')
    def logout(self):
        pass


class Steps(__Base):
    @allure.step('Нажимаем на кнопку {1}')
    def click_button(self, name):
        pass

    @allure.step('Расскрываем список {1}')
    def click_on_dropdown(self, name):
        pass

    @allure.step('Выбираем {0}')
    def choose_in_dropdown(self, name):
        pass

    # дальше шаги будут описывать по мере необходимости
