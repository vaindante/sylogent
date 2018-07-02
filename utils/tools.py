from selenium.common.exceptions import NoAlertPresentException


def close_popups(instance):
    try:
        alert = instance.switch_to.alert
        if alert is not None:
            alert.accept()
    except NoAlertPresentException:
        pass
