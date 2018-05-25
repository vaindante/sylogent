import pytest


@pytest.allure.story('Procedure  Test Suite QATA - 20')
@pytest.mark.test_20
def test_qata_20(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')

    frontend.navigate('Project')
    frontend.choose_tab('Create')

    frontend.choose_checkbox('Abstract Restyle and Resubmit')
    frontend.choose_checkbox('Allow selection of any study', test=True)
    frontend.choose_on_table('ADD NAME FOR 13325')

    frontend.click_button('btnSaveAndCloseStudies')
    frontend.click_button_on_modal_dialog('No')
