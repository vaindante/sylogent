from time import sleep

import pytest



@pytest.fixture()
def prepare(frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')


@pytest.allure.story('QA-PS-01-Application-UAT-Verification - Full Regression Test Suite')
@pytest.mark.test_01
@pytest.mark.tmp
@pytest.mark.usefixtures('prepare')
@pytest.mark.parametrize('nav', ('Tasks', 'Projects', 'Targets', 'Studies', 'Resources/Authors', 'Reports'))
def test_qata_01(log, frontend, nav):
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
    sleep(3)


    frontend.navigate('Calendar')
    log.attach_selenium_screenshot('calendar', frontend.driver)