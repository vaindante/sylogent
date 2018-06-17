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
@pytest.mark.tmp
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
@pytest.mark.tmp
@pytest.mark.usefixtures('prepare')
def test_qata_02(log, frontend):
    frontend.navigate('Project')
    frontend.choose_tab('Create')
    log.attach_selenium_screenshot('PROJECT TYPE selection', frontend.driver)

    frontend.choose_checkbox('Abstract Restyle and Resubmit')
    frontend.choose_checkbox('Allow selection of any study', test=True)
    frontend.choose_on_table('ADD NAME FOR 13325')

    frontend.click_button('btnSaveStudies')
    frontend.click_button_on_modal_dialog('Yes')

    frontend.fill_table(
        {
            'Title': 'Test_June01',
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
    with pytest.raises(ZeroDivisionError):
        1/0

    frontend.click_button('btnSaveTasksAndResources')
    frontend.click_button('PageFrame1_btnFinish')
    frontend.navigate('Projects')
    frontend.click_button('All')
    sleep(3)


# frontend._browser.close_all_popups()
# Ждем окончания запросов

# frontend._browser.close_all_popups()

@pytest.mark.test_1
def test_qata_1(frontend):
    pass
