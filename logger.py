import json
import logging
import os
import sys
from io import StringIO

import pytest
from allure.constants import AttachmentType

_beautiful_json = dict(indent=2, ensure_ascii=False, sort_keys=True)

# LOGGING console ####################################################################################################
# Резервируем имя для кастомного уровня логгирования
logging.addLevelName(15, "SUBDEBUG")
logging.addLevelName(5, "TEST")

# Форматирование лога
log_formatter = logging.Formatter("%(asctime)s [%(threadName)s] [%(levelname)s] - %(message)s",
                                  datefmt='%Y-%m-%d %H:%M:%S')


class CustomLogger(logging.Logger):
    test_log = StringIO()

    # Метод форматирования сообщения
    @staticmethod
    def format_message(message):
        return json.dumps(message, **_beautiful_json) if isinstance(message, (dict, list, tuple)) else str(message)

    # Кастомный уровень логирования
    def subdebug(self, message, *args, **kwargs):
        if self.isEnabledFor(15):
            self._log(15, message, args, **kwargs)

    # Метод для прикрепления данных к репорту (завязали на единый класс)
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
                self.debug('Attach screenshot')
                self.attach_png(attach_name, selenium_driver.get_screenshot_as_png())
                self.debug('...Done')
            except Exception as e:
                self.error('Cannot get screenshot from SeleniumWebDriver')
                pytest.allure.attach(attach_name, str(e))

        else:
            self.error('Нет браузера')

    def add_handler(self, file_name, mode='a'):
        file_handler = logging.FileHandler(filename=file_name, mode=mode)
        file_handler.setFormatter(log_formatter)
        file_handler.setLevel(os.getenv('LOGGING_LEVEL_TO_CONSOLE', 'WARN'))
        self.addHandler(file_handler)


def setup_logging():
    # Настройка логирования
    logger = CustomLogger('root')

    # Уровень вывода
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(os.getenv('LOGGING_LEVEL_TO_CONSOLE', 'WARN'))
    # Устанавливаем формат сообщений
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

    # Уровень вывода
    string_io = logging.StreamHandler(logger.test_log)
    string_io.setLevel(os.getenv('LOGGING_LEVEL', 'INFO'))
    # Устанавливаем формат сообщений
    string_io.setFormatter(log_formatter)
    logger.addHandler(string_io)
    return logger


logger = setup_logging()
