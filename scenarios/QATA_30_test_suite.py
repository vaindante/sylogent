import pytest


def get_values(driver, xpath, atr):
    els = driver.get_by_xpath(xpath, is_elements_list=True)
    return [v.get_attribute(atr) for v in els]


@pytest.allure.story('Task Filters Validation')
@pytest.mark.test_30
def test_qata_30(log, frontend):
    frontend.open_url('https://rc.sylogent.com/ps/Landing/Login.aspx')
    frontend.authorization.login(frontend.login, frontend.passwd)
    frontend.goto('PubSTRAT')

    frontend.click_on_dropdown('Product')
    frontend.choose_in_dropdown('Program QA')

    frontend.navigate('Administration')
    assert {
        'General', 'Audiences', 'Custom', 'Fields', 'System', 'Field', 'End', 'States', 'Indications', 'Notifications',
        'Workflows', 'Resources/Authors', 'Resource', 'Types', 'Resource', 'Groups', 'Segments', 'Sponsors', 'Study',
        'Setup', 'Budget'
    }.difference(get_values(frontend._browser, '//div[@class="Mid"]/a', 'text'))

    frontend.navigate('General')
    frontend.wait(2)

    assert {
        'Tasks', 'Projects', 'Targets', 'Studies', 'Resources/Authors', 'Reports', 'Admin'
    }.difference(get_values(frontend._browser, '//*[@id="programname"]/parent::td/../td//a', 'text'))

    frontend.click_button('add new', text=True)
    frontend.fill_table(
        {
            'StartDate$Date': '12/12/2018',
            'EndDate$Date': '25/12/2018',
            'Description': 'test'
        },
        type_='input'
    )
    frontend.click_button('submit', text=True)