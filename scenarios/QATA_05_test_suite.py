from time import sleep

import pytest


@pytest.allure.story('Projects - "Active"  Filters Validation')
@pytest.mark.test_05
def test_qata_01(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')
    sleep(3)

    frontend.navigate('Projects')
    frontend.choose_tab('Active')

    #frontend.set_filter('Project Id', 'FilterProjectId')

    #log.attach_selenium_screenshot('Project Id Filter', frontend.driver)
    #frontend.click_on_button('ctl00$Main$ctl04')

