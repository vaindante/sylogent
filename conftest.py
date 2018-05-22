import os
import shutil
import subprocess
import threading

import pytest

from core.connections.driver import SeleniumWebDriver
from core.selenium_steps import Frontend
from logger import logger


########################################################################################################################
# py.scenarios conf

def pytest_configure(config):
    logger.info('Start py.scenarios configuring')

    if os.getenv('GENERATE_REPORT', True):
        # Prepare reports dir
        reports_dir = 'reports'

        logger.info("delete report dir")

        try:
            shutil.rmtree(reports_dir)
            logger.info('  ... already deletes')
        except FileNotFoundError:
            pass
        finally:
            os.makedirs(reports_dir)
            logger.info('  ... create report dir')

    logger.info('Start executing:')


########################################################################################################################
@pytest.fixture(scope='session')
def log():
    return logger


@pytest.yield_fixture(scope="session")
def _browser():
    logger.info('Selenium: open browser')
    url = os.getenv('URL', 'https://rc.sylogent.com/ps/Landing/Login.aspx')
    browser_binding = SeleniumWebDriver()
    # Сохраняем уникальный id окна and url
    browser_binding.window = {
        'window': browser_binding.driver.window_handles[0],
        'url': url
    }

    # Очищаем куки, открываем или перезагружаем страницу
    browser_binding.delete_all_cookies()
    browser_binding.open_url(url)
    browser_binding.get_cookies()

    yield browser_binding

    logger.info('Selenium: close browser')
    browser_binding.quit()


@pytest.fixture(scope='function')
def frontend(_browser):
    # Возможно надо будет чистить куки, и еще что-нибудь
    return Frontend(_browser)


########################################################################################################################
# Hooks

# Called before fixtures
def pytest_runtest_setup(item):
    print('\n')
    threading.current_thread()._name = item.name
    logger.test_log.truncate(0)
    logger.test_log.seek(0)
    logger.info('==== Run fixtures ====:')


# Called to execute the scenarios item
def pytest_runtest_call(item):
    logger.info('=======================')
    logger.info('Run scenarios')


# After scenarios, before fixture ends
def pytest_runtest_teardown(item, nextitem):
    print('\n')
    logger.info('Stop scenarios')
    logger.info('==== Stop fixtures ====')


def pytest_runtest_makereport(item, call):
    # if scenarios result has fail
    logger.attach_error('logs', logger.test_log.getvalue())
    if '_browser' in item._request._funcargs:
        logger.attach_selenium_screenshot('screenshot', item._request._funcargs['_browser'].driver)


def pytest_unconfigure(config):
    if os.getenv('GENERATE_REPORT', True):
        threading.current_thread()._name = 'Report'
        logger.info('### Create allure report ')
        try:
            subprocess.check_call('allure generate -c reports', shell=True)

        except subprocess.CalledProcessError:
            logger.warning('!!! allure: cannot create report - report dir is empty')
