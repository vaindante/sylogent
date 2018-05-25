from time import sleep

from core.frontend import *
from logger import logger


class Frontend:
    def __init__(self, browser, l, p):
        self._browser, self.login, self.passwd = browser, l, p
        self.authorization = Authorization(browser)
        self.__steps = Steps(browser)
        self.open_url = self._browser.open_url
        logger.debug('frontend build completed')

    def __getattr__(self, item):
        # TODO: for debug
        sleep(.5)
        return getattr(self.__steps, item)

    @property
    def driver(self):
        return self._browser.driver
