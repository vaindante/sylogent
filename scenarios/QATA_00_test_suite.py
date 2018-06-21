import pytest


@pytest.mark.demo
def test_qata_02(log, frontend, test_user):
    log.attach_error(test_user['username'], test_user)
    frontend.open_url(test_user['url'])
    frontend.authorization.login(test_user['username'], test_user['password'])
