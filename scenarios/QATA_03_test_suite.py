from time import sleep

import pytest


@pytest.allure.story('Task Filters Validation')
@pytest.mark.test_07
def test_qata_07(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')
    sleep(3)
    frontend.navigate('Tasks')

    frontend.set_filter('Project Id', 'FilterProjectId')

    #frontend.click_on_button('ctl00$Main$ctl04')

    # assert any('External' == v for v in frontend.get_values_on_table(8))
    frontend.goto('ClearFilter')

    frontend.set_filter('Req', 'FilterReq')
    frontend.click_button('cbReq')

    #frontend.click_button('Clear Filters', text=True)

