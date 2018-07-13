from time import sleep

import pytest


@pytest.allure.story('Reports -Table Filters Validation')
@pytest.mark.test_06
def test_qata_01(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')
    sleep(3)

    frontend.navigate('Reports')
    frontend.set_filter('Name', 'FilterName')
    frontend.goto('ClearFilter')

    log.attach_selenium_screenshot('Reports Table Filters Validation', frontend.driver)


    frontend.set_filter('Description', 'FilterDescription')
    frontend.goto('ClearFilter')

    frontend.set_filter('Role', 'FilterRole')
    frontend.goto('ClearFilter')

@pytest.allure.story('Reports/Dashboards -Table Filters Validation')
@pytest.mark.test_06
def test_qata_02(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')
    sleep(3)

    frontend.navigate('Reports')
    frontend.choose_tab('Dashboards')
    frontend.set_filter('Name', 'FilterName')
    frontend.goto('ClearFilter')

    log.attach_selenium_screenshot('Reports/Dashboards Filters', frontend.driver)


    frontend.set_filter('Description', 'FilterDescription')
    frontend.goto('ClearFilter')

    frontend.set_filter('Role', 'FilterRole')
    frontend.goto('ClearFilter')

@pytest.allure.story('Reports/Alerts -Table Filters Validation')
@pytest.mark.test_06
def test_qata_03(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')
    sleep(3)

    frontend.navigate('Reports')
    frontend.choose_tab('Alerts')
    frontend.set_filter('Name', 'FilterName')
    frontend.goto('ClearFilter')

    log.attach_selenium_screenshot('Reports/Alerts Filters', frontend.driver)


    frontend.set_filter('Description', 'FilterDescription')
    frontend.goto('ClearFilter')

    frontend.set_filter('Role', 'FilterRole')
    frontend.goto('ClearFilter')

    frontend.set_filter('Status', 'FilterStatus')
    frontend.goto('ClearFilter')

