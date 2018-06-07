import pytest


@pytest.fixture()
def prepare(frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')


@pytest.allure.story('Procedure  Test Suite QATA - 01')
@pytest.mark.test_01
@pytest.mark.parametrize('nav', ('Tasks', 'Projects', 'Targets', 'Studies', 'Resources/Authors', 'Reports'))
def test_qata_01(log, frontend, nav, prepare):
    frontend.navigate(nav)
    frontend.navigate('Tasks')

    frontend.click_button('Active')
    frontend.click_button('Future')

    log.attach_selenium_screenshot('tasks', frontend.driver)

    frontend.navigate('Projects')

    log.attach_selenium_screenshot('projects', frontend.driver)

    # frontend.driver.switch_to_popap
    frontend.navigate('Targets')
    if nav == '':
        log.attach_selenium_screenshot('targets', frontend.driver)

    frontend.navigate('Studies')
    log.attach_selenium_screenshot('studies', frontend.driver)

    frontend.navigate('Resources/Authors')
    log.attach_selenium_screenshot('resources/authors', frontend.driver)

    frontend.navigate('Reports')
    log.attach_selenium_screenshot('reports', frontend.driver)


@pytest.mark.deb
def test_qata_20_2(prepare, frontend, log):
    frontend.navigate('Tasks')

    frontend.click_button('Active')
    frontend.click_button('Future')


@pytest.mark.deb
def test_qata_20_3(prepare, frontend, log):
    frontend.navigate('Studies')
