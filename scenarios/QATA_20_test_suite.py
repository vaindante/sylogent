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

    frontend.click_button('btnSaveStudies')
    frontend.click_button_on_modal_dialog('Yes')

    frontend.fill_table(
        {
            'Title': 'Test_May01',
            'Project Champion Message': 'Audit, Jim – Austria',
        }
    )
    frontend.choose_on_dropdown_in_table('Project Champion', 'Audit, Jim - Austria')
    # frontend.choose_on_dropdown_in_table('Language', 'English', _id='10594')

    frontend.click_button('btnSaveGeneral')
    # frontend.click_button_on_modal_dialog('Yes')

    frontend.click_button('PageFrame1_btnSaveTarget')
    # frontend.click_button_on_modal_dialog('Yes')

    frontend.set_checkbox_in_table('Deadline Can Slip', True)
    frontend.click_button('PageFrame1_btnSaveTimeLine')

    frontend.choose_checkbox('ow selection of any clinical finding', test=True)
    frontend.click_button('PageFrame1_btnSaveClinicalFindings')

    frontend.choose_on_dropdown_in_table('Lead Author', 'Admin, Sylogent')
    frontend.choose_authors('Other Authors', ('Mark',))
    frontend.click_button('PageFrame1_btnSaveAuthors')

    frontend.config_task(
        'Task 1',
        {
            'Admin, Sylogent': 'req'
        }
    )
    frontend.click_button('btnSaveTasksAndResources')
    frontend.click_button('PageFrame1_btnFinish')
