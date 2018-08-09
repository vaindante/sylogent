import pytest


@pytest.allure.story('Resources/Authors - filters functionality validation scenario')
@pytest.mark.test_03
def test_qata_01(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')


    frontend.navigate('Resources/Authors')

    frontend.set_filter('Name', "FilterName")
    log.attach_selenium_screenshot('Name filter', frontend.driver)
    frontend.goto('ClearFilter')


    frontend.set_filter('Email', "FilterEmail")
    log.attach_selenium_screenshot('Filter Email ', frontend.driver)
    frontend.goto('ClearFilter')


    frontend.set_filter('Country', "FilterCountry")
    log.attach_selenium_screenshot('Filter Country ', frontend.driver)
    frontend.goto('ClearFilter')

    frontend.set_filter('Company', "FilterCompany")
    log.attach_selenium_screenshot('Filter Company', frontend.driver)
    frontend.goto('ClearFilter')

    frontend.set_filter('Access Type', "FilterAccessTypes")
    log.attach_selenium_screenshot('Filter Access Types', frontend.driver)
    frontend.goto('ClearFilter')


    frontend.set_filter('Resource Type', "FilterResourceType")
    log.attach_selenium_screenshot('Filter Resource Type', frontend.driver)
    frontend.goto('ClearFilter')

    frontend.set_filter('Status', "FilterDisabled")
    log.attach_selenium_screenshot('Filter for Status', frontend.driver)
    frontend.goto('ClearFilter')


    frontend.set_filter('Membership', 'cbExternal')
    log.attach_selenium_screenshot('Resources/Authors filters validation', frontend.driver)

    assert any('External' == v for v in frontend.get_values_on_table(8))
    frontend.click_button('ClearFilter')
    # frontend.click_button('Clear Filters', text=True)

    frontend.navigate('Resources/Authors')
    frontend.set_filter('Membership', 'ctl00_Main_cbInternal')
    assert any('Internal' == v for v in frontend.get_values_on_table(8))
    frontend.click_button('ClearFilter')
    # frontend.click_button('Clear Filters', text=True)