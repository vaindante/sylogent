import pytest
import os
from utils.object import correspond_selected_object


@pytest.allure.feature('Feature1')
@pytest.allure.story('Story1')
@pytest.mark.smoke
@pytest.mark.test_set_one
class TestSetOneOne:
    @pytest.mark.test_1
    @pytest.mark.case_1
    def test_login(self, log, frontend):
        frontend.authorization.login(os.getenv('LOGIN', 'test'), os.getenv('PASSWD', 'test'))
        frontend.authorization.logout()
        # log.attach_selenium_screenshot('test_1', frontend.driver)

    @pytest.mark.test_2
    def test_test(self, frontend, log):
        with pytest.allure.step('Авторизуемся на сайте'):
            frontend.authorization.login('test@test.ru', 'test')
            log.attach_selenium_screenshot('Test', frontend.driver)

        with pytest.allure.step('Проект'):
            with pytest.allure.step('Go to  PubStrat'):
                frontend.click_on_dropdown('Product')
                frontend.choose_in_dropdown('Product QA')
                frontend.click_button('test')
            with pytest.allure.step('CREATE A PROJECT'):
                frontend.click_on_dropdown('test1')
                frontend.choose_in_dropdown('test2')
                frontend.click_button('test3')
        with pytest.allure.step('Test fail'):
            correspond_selected_object(
                {
                    'a': 1,
                    'b': 2,
                    'c': 3,
                    'd': 4,
                },
                {
                    'a': 1,
                    'b': 21,
                    'c': 3,
                },

            )


@pytest.allure.feature('Feature1')
@pytest.allure.story('Story2')
@pytest.mark.smoke
@pytest.mark.test_set_one
class TestSetOneTwo:
    @pytest.mark.test_1
    def test_login(self, frontend):
        frontend.authorization.login('test@test.ru', 'test')
        frontend.authorization.logout()

    @pytest.mark.test_2
    def test_test(self, frontend, log):
        with pytest.allure.step('Авторизуемся на сайте'):
            frontend.authorization.login('test@test.ru', 'test')
            log.attach_selenium_screenshot('Test', frontend.driver)

        with pytest.allure.step('Проект'):
            with pytest.allure.step('Go to  PubStrat'):
                frontend.click_on_dropdown('Product')
                frontend.choose_in_dropdown('Product QA')
                frontend.click_button('test')
            with pytest.allure.step('CREATE A PROJECT'):
                frontend.click_on_dropdown('test1')
                frontend.choose_in_dropdown('test2')
                frontend.click_button('test3')
        with pytest.allure.step('Test fail'):
            correspond_selected_object(
                {
                    'a': 1,
                    'b': 2,
                    'c': 3,
                    'd': 4,
                },
                {
                    'a': 1,
                    'b': 21,
                    'c': 3,
                },

            )


@pytest.allure.feature('Feature1')
@pytest.allure.story('Story3')
@pytest.mark.smoke
@pytest.mark.test_set_one
class TestSetOneThree:
    @pytest.mark.test_1
    def test_login(self, frontend):
        frontend.authorization.login('test@test.ru', 'test')
        frontend.authorization.logout()

    @pytest.mark.test_2
    def test_test(self, frontend, log):
        with pytest.allure.step('Авторизуемся на сайте'):
            frontend.authorization.login('test@test.ru', 'test')
            log.attach_selenium_screenshot('Test', frontend.driver)

        with pytest.allure.step('Проект'):
            with pytest.allure.step('Go to  PubStrat'):
                frontend.click_on_dropdown('Product')
                frontend.choose_in_dropdown('Product QA')
                frontend.click_button('test')
            with pytest.allure.step('CREATE A PROJECT'):
                frontend.click_on_dropdown('test1')
                frontend.choose_in_dropdown('test2')
                frontend.click_button('test3')
        with pytest.allure.step('Test fail'):
            correspond_selected_object(
                {
                    'a': 1,
                    'b': 2,
                    'c': 3,
                    'd': 4,
                },
                {
                    'a': 1,
                    'b': 21,
                    'c': 3,
                },

            )


@pytest.allure.feature('Feature2')
@pytest.allure.story('Story1')
@pytest.mark.smoke
@pytest.mark.test_set_two
class TestSetTwoOne:
    @pytest.mark.test_1
    def test_login(self, frontend):
        frontend.authorization.login('test@test.ru', 'test')
        frontend.authorization.logout()

    @pytest.mark.test_2
    def test_test(self, frontend, log):
        with pytest.allure.step('Авторизуемся на сайте'):
            frontend.authorization.login('test@test.ru', 'test')
            log.attach_selenium_screenshot('Test', frontend.driver)

        with pytest.allure.step('Проект'):
            with pytest.allure.step('Go to  PubStrat'):
                frontend.click_on_dropdown('Product')
                frontend.choose_in_dropdown('Product QA')
                frontend.click_button('test')
            with pytest.allure.step('CREATE A PROJECT'):
                frontend.click_on_dropdown('test1')
                frontend.choose_in_dropdown('test2')
                frontend.click_button('test3')
        with pytest.allure.step('Test fail'):
            correspond_selected_object(
                {
                    'a': 1,
                    'b': 2,
                    'c': 3,
                    'd': 4,
                },
                {
                    'a': 1,
                    'b': 21,
                    'c': 3,
                },

            )


@pytest.allure.feature('Feature2')
@pytest.allure.story('Story3')
@pytest.mark.smoke
@pytest.mark.test_set_two
class TestSetTwoTwo:
    @pytest.mark.test_1
    def test_login(self, frontend):
        frontend.authorization.login('test@test.ru', 'test')
        frontend.authorization.logout()

    @pytest.mark.test_2
    def test_test(self, frontend, log):
        with pytest.allure.step('Авторизуемся на сайте'):
            frontend.authorization.login('test@test.ru', 'test')
            log.attach_selenium_screenshot('Test', frontend.driver)

        with pytest.allure.step('Проект'):
            with pytest.allure.step('Go to  PubStrat'):
                frontend.click_on_dropdown('Product')
                frontend.choose_in_dropdown('Product QA')
                frontend.click_button('test')
            with pytest.allure.step('CREATE A PROJECT'):
                frontend.click_on_dropdown('test1')
                frontend.choose_in_dropdown('test2')
                frontend.click_button('test3')
        with pytest.allure.step('Test fail'):
            correspond_selected_object(
                {
                    'a': 1,
                    'b': 2,
                    'c': 3,
                    'd': 4,
                },
                {
                    'a': 1,
                    'b': 21,
                    'c': 3,
                },

            )


@pytest.allure.feature('Feature2')
@pytest.allure.story('Story2')
@pytest.mark.smoke
@pytest.mark.test_set_two
class TestSetTwoThree:
    @pytest.mark.test_1
    def test_login(self, frontend):
        frontend.authorization.login('test@test.ru', 'test')
        frontend.authorization.logout()

    @pytest.mark.test_2
    def test_test(self, frontend, log):
        with pytest.allure.step('Авторизуемся на сайте'):
            frontend.authorization.login('test@test.ru', 'test')
            log.attach_selenium_screenshot('Test', frontend.driver)

        with pytest.allure.step('Проект'):
            with pytest.allure.step('Go to  PubStrat'):
                frontend.click_on_dropdown('Product')
                frontend.choose_in_dropdown('Product QA')
                frontend.click_button('test')
            with pytest.allure.step('CREATE A PROJECT'):
                frontend.click_on_dropdown('test1')
                frontend.choose_in_dropdown('test2')
                frontend.click_button('test3')
        with pytest.allure.step('Test fail'):
            correspond_selected_object(
                {
                    'a': 1,
                    'b': 2,
                    'c': 3,
                    'd': 4,
                },
                {
                    'a': 1,
                    'b': 21,
                    'c': 3,
                },

            )
