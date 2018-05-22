from core.frontend import *
from logger import logger


class Frontend:
    def __init__(self, browser):
        self._browser = browser
        self.authorization = Authorization(browser)
        self.__steps = Steps(browser)
        logger.debug('frontend build completed')

    def __getattr__(self, item):
        return getattr(self.__steps, item)

    @property
    def driver(self):
        return self._browser.driver
