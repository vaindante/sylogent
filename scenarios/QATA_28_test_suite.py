from time import sleep

import pytest

from utils.tools import close_popups


@pytest.allure.story('Create project :Abstract Restyle and Resubmit - Project Wizard functionality verification')
@pytest.mark.test_28
def test_qata_01(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')

    frontend.navigate('Project')
    log.attach_selenium_screenshot('Project Wizard', frontend.driver)
    frontend.choose_tab('Create')
    log.attach_selenium_screenshot('TYPE', frontend.driver)

    frontend.choose_checkbox('Abstract Restyle and Resubmit')
    # frontend.choose_checkbox('Allow selection of any study', test=True)
    # frontend.choose_on_table('ADD NAME FOR 13329')

    log.attach_selenium_screenshot('STUDIES', frontend.driver)

    frontend.click_button('btnSaveStudies')
    frontend.click_button_on_modal_dialog('Yes')

    frontend.fill_table(
        {
            'Title': 'Test_July_2018- do not remove',
            'Project Champion Message': 'Audit, Jim – Austria',
        }
    )
    frontend.choose_on_dropdown_in_table('Project Champion', 'Audit, Jim - Austria')
    # frontend.choose_on_dropdown_in_table('Language', 'English', _id='10594')
    log.attach_selenium_screenshot('GENERAL', frontend.driver)

    frontend.click_button('btnSaveGeneral')
    # frontend.click_button_on_modal_dialog('Yes')

    frontend.click_button('PageFrame1_btnSaveTarget')
    # frontend.click_button_on_modal_dialog('Yes')
    log.attach_selenium_screenshot('TARGET tab', frontend.driver)

    frontend.set_checkbox_in_table('Deadline Can Slip', True)
    log.attach_selenium_screenshot('TIMELINE', frontend.driver)
    frontend.click_button('PageFrame1_btnSaveTimeLine')

    frontend.choose_checkbox('ow selection of any clinical finding', test=True)
    log.attach_selenium_screenshot('CLINICAL FINDINGS', frontend.driver)
    frontend.click_button('PageFrame1_btnSaveClinicalFindings')

    frontend.choose_on_dropdown_in_table('Lead Author', 'Admin, Sylogent')
    frontend.choose_authors('Other Authors', ('Mark',))
    log.attach_selenium_screenshot('AUTHORS', frontend.driver)
    frontend.click_button('PageFrame1_btnSaveAuthors')

    frontend.config_task(
        'Task 1',
        {
            'Admin, Sylogent': 'req'
        }
    )
    log.attach_selenium_screenshot('TASKS AND RESOURCES', frontend.driver)
    frontend.click_button('btnSaveTasksAndResources')
    log.attach_selenium_screenshot('SUMMARY', frontend.driver)
    frontend.click_button('PageFrame1_btnFinish')
    sleep(3)

    close_popups(frontend.driver)