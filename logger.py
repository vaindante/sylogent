import json
import logging
import os
import sys
from io import StringIO

import pytest
from allure.constants import AttachmentType

from utils.tools import close_popups

_beautiful_json = dict(indent=2, ensure_ascii=False, sort_keys=True)

# LOGGING console ####################################################################################################
# Reserved name for custom logging
logging.addLevelName(15, "SUBDEBUG")
logging.addLevelName(5, "TEST")

# Logger formating
log_formatter = logging.Formatter("%(asctime)s [%(threadName)s] [%(levelname)s] - %(message)s",
                                  datefmt='%Y-%m-%d %H:%M:%S')


class CustomLogger(logging.Logger):
    test_log = StringIO()

    # Metod formating message
    @staticmethod
    def format_message(message):
        return json.dumps(message, **_beautiful_json) if isinstance(message, (dict, list, tuple)) else str(message)

    # Custom level of logging
    def subdebug(self, message, *args, **kwargs):
        if self.isEnabledFor(15):
            self._log(15, message, args, **kwargs)

    # Method to attached data to report (one class dependency)
    def attach_debug(self, name, message):
        if self.isEnabledFor(10):
            pytest.allure.attach(name, self.format_message(message))

    def attach_subdebug(self, name, message):
        if self.isEnabledFor(15):
            pytest.allure.attach(name, self.format_message(message))

    def attach_info(self, name, message):
        if self.isEnabledFor(20):
            pytest.allure.attach(name, self.format_message(message))

    def attach_error(self, name, message):
        pytest.allure.attach(name, self.format_message(message))

    @staticmethod
    def attach_png(name, message):
        pytest.allure.attach(name, message, type=AttachmentType.PNG)

    def attach_selenium_screenshot(self, attach_name, selenium_driver):
        if selenium_driver:
            try:
                close_popups(selenium_driver)
                self.debug('Attach screenshot')
                self.attach_png(attach_name, selenium_driver.get_screenshot_as_png())
                self.debug('...Done')
            except Exception as e:
                self.error('Cannot get screenshot from SeleniumWebDriver')
                pytest.allure.attach(attach_name, str(e))

        else:
            self.error('No browser is define')

    def add_handler(self, file_name, mode='a'):
        file_handler = logging.FileHandler(filename=file_name, mode=mode)
        file_handler.setFormatter(log_formatter)
        file_handler.setLevel(os.getenv('LOGGING_LEVEL_TO_CONSOLE', 'WARN'))
        self.addHandler(file_handler)


def setup_logging():
    # Logging setup
    logger = CustomLogger('root')

    # Level of handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(os.getenv('LOGGING_LEVEL_TO_CONSOLE', 'WARN'))
    # Create a method of message
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

    # Level of handler
    string_io = logging.StreamHandler(logger.test_log)
    string_io.setLevel(os.getenv('LOGGING_LEVEL', 'INFO'))
    # Create a method of message
    string_io.setFormatter(log_formatter)
    logger.addHandler(string_io)
    return logger


logger = setup_logging()
