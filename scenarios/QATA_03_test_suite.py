from time import sleep

import pytest


@pytest.allure.story('Tasks - "To Do"  Filters Validation')
@pytest.mark.test_04
def test_qata_01(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')
    sleep(3)
    frontend.navigate('Tasks')

    frontend.set_filter('Project Id', 'FilterProjectId')

    log.attach_selenium_screenshot('Project Id Filter', frontend.driver)
    #frontend.click_on_button('ctl00$Main$ctl04')

    # assert any('External' == v for v in frontend.get_values_on_table(8))
    frontend.goto('ClearFilter')

    frontend.set_filter('Req', 'FilterReq')
    #frontend.click_button('cbReq', text=True)
    log.attach_selenium_screenshot('Req Filter', frontend.driver)
    frontend.goto('ClearFilter')
    #frontend.click_button('Clear Filters', text=True)

    frontend.set_filter('Due Date', "FilterDueDate")
    log.attach_selenium_screenshot('Due Date', frontend.driver)
    frontend.goto('ClearFilter')

    frontend.set_filter('Task', "FilterTasks")
    log.attach_selenium_screenshot('Task', frontend.driver)
    frontend.goto('ClearFilter')

    frontend.set_filter('Product', "FilterProduct")
    log.attach_selenium_screenshot('Filter Product', frontend.driver)
    frontend.goto('ClearFilter')

    frontend.goto ('FilterProject')
    log.attach_selenium_screenshot('Filter Project', frontend.driver)
    frontend.goto('ClearFilter')




@pytest.allure.story('Tasks - "Planned"  Filters Validation')
@pytest.mark.test_04
def test_qata_02(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')
    sleep(3)
    frontend.navigate('Tasks')
    frontend.goto('listTaskFuture')

    frontend.set_filter('Project Id', 'FilterProjectId')

    log.attach_selenium_screenshot('Project Id Filter', frontend.driver)
    #frontend.click_on_button('ctl00$Main$ctl04')

    # assert any('External' == v for v in frontend.get_values_on_table(8))
    frontend.goto('ClearFilter')

    frontend.set_filter('Req', 'FilterReq')
    #frontend.click_button('cbReq', text=True)
    log.attach_selenium_screenshot('Req Filter', frontend.driver)
    frontend.goto('ClearFilter')
    #frontend.click_button('Clear Filters', text=True)

    frontend.set_filter('Due Date', "FilterDueDate")
    log.attach_selenium_screenshot('Due Date', frontend.driver)
    frontend.goto('ClearFilter')

    frontend.set_filter('Task', "FilterTasks")
    log.attach_selenium_screenshot('Task', frontend.driver)
    frontend.goto('ClearFilter')

    frontend.set_filter('Product', "FilterProduct")
    log.attach_selenium_screenshot('Filter Product', frontend.driver)
    frontend.goto('ClearFilter')

    frontend.goto ('FilterProject')
    log.attach_selenium_screenshot('Filter Project', frontend.driver)
    frontend.goto('ClearFilter')

@pytest.allure.story('Tasks - "Done"  Filters Validation')
@pytest.mark.test_04
def test_qata_03(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')
    sleep(3)
    frontend.navigate('Tasks')
    frontend.goto('listTaskDone')

    frontend.set_filter('Project Id', 'FilterProjectId')

    log.attach_selenium_screenshot('Project Id Filter', frontend.driver)
    #frontend.click_on_button('ctl00$Main$ctl04')

    # assert any('External' == v for v in frontend.get_values_on_table(8))
    frontend.goto('ClearFilter')

    frontend.set_filter('Req', 'FilterReq')
    #frontend.click_button('cbReq', text=True)
    log.attach_selenium_screenshot('Req Filter', frontend.driver)
    frontend.goto('ClearFilter')
    #frontend.click_button('Clear Filters', text=True)


    frontend.set_filter('Completed', "FilterCompletionDate")
    log.attach_selenium_screenshot('Completed', frontend.driver)
    frontend.goto('ClearFilter')

    frontend.set_filter('Task', "FilterTasks")
    log.attach_selenium_screenshot('Task', frontend.driver)
    frontend.goto('ClearFilter')

    frontend.set_filter('Product', "FilterProduct")
    log.attach_selenium_screenshot('Filter Product', frontend.driver)
    frontend.goto('ClearFilter')

    frontend.goto ('FilterProject')
    log.attach_selenium_screenshot('Filter Project', frontend.driver)
    frontend.goto('ClearFilter')