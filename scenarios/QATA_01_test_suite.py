import pytest
from time import sleep

import pytest


@pytest.fixture()
def prepare(frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')


@pytest.allure.story('QA-PS-01-Application-UAT-Verification')
@pytest.mark.test_01
#@pytest.mark.tmp
@pytest.mark.parametrize('nav', ('Tasks', 'Projects', 'Targets', 'Studies', 'Resources/Authors', 'Reports'))
def test_qata_01(log, frontend, nav, prepare):
    frontend.navigate(nav)
    frontend.navigate('Tasks')

    frontend.goto('listTaskActive')
    frontend.goto('listTaskFuture')
    frontend.goto('listTaskDone')

    log.attach_selenium_screenshot('tasks', frontend.driver)

    frontend.navigate('Projects')

    frontend.choose_tab('Active')
    frontend.choose_tab('Planned')
    frontend.choose_tab('Done')
    frontend.choose_tab('All')

    log.attach_selenium_screenshot('projects', frontend.driver)

    # frontend.driver.switch_to_popap
    frontend.navigate('Targets')
    frontend.choose_tab('Conferences')
    if nav == '':
        log.attach_selenium_screenshot('targets', frontend.driver)

    frontend.navigate('Studies')
    frontend.choose_tab('Create')
    frontend.choose_tab('Import')
    log.attach_selenium_screenshot('studies', frontend.driver)

    frontend.navigate('Resources/Authors')
    frontend.choose_tab('Documents')
    log.attach_selenium_screenshot('resources/authors', frontend.driver)

    frontend.navigate('Reports')
    frontend.choose_tab('Alerts')
    log.attach_selenium_screenshot('reports', frontend.driver)

    frontend.navigate('Calendar')
    log.attach_selenium_screenshot('calendar', frontend.driver)



# @pytest.mark.deb
# def test_qata_20_2(prepare, frontend, log):
#     frontend.navigate('Tasks')
#
#     frontend.click_button('Active')
#     frontend.click_button('Future')
#
#
# # @pytest.mark.deb
# def test_qata_20_3(prepare, frontend, log):
#     frontend.navigate('Studies')

@pytest.allure.story('QA-PS-28-Create:Restyle and Resubmit Project ')
@pytest.mark.test_02
#@pytest.mark.tmp
@pytest.mark.usefixtures('prepare')
def test_qata_02(log, frontend):

    frontend.navigate('Project')
    log.attach_selenium_screenshot('Project Wizard', frontend.driver)
    frontend.choose_tab('Create')
    log.attach_selenium_screenshot('TYPE', frontend.driver)

    frontend.choose_checkbox('Abstract Restyle and Resubmit')
    #frontend.choose_checkbox('Allow selection of any study', test=True)
    #frontend.choose_on_table('ADD NAME FOR 13329')

    log.attach_selenium_screenshot('STUDIES', frontend.driver)

    frontend.click_button('btnSaveStudies')
    frontend.click_button_on_modal_dialog('Yes')

    frontend.fill_table(
        {
            'Title': 'Test_June14/2018- do not remove',
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


    frontend.click_button('All')


    frontend._browser.close_all_popups()

@pytest.mark.test_1
def test_qata_1(frontend):
    pass
