import pytest


@pytest.allure.story('Procedure  Test Suite QATA - 22')
@pytest.mark.test_22
def test_qata_22(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')

    frontend.navigate('Resources/Authors')
    frontend.set_filter('Membership', 'cbExternal')
    assert any('External' == v for v in frontend.get_values_on_table(8))
    frontend.click_button('Clear Filters', text=True)

    frontend.navigate('Resources/Authors')
    frontend.set_filter('Membership', 'ctl00_Main_cbInternal')
    assert any('Internal' == v for v in frontend.get_values_on_table(8))
    frontend.click_button('Clear Filters', text=True)
