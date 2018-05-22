# Custom exceptions classes
import json

from logger import logger


def json_to_stderr(message_json):
    if type(message_json) is set:
        message_json = list(message_json)

    try:
        json_text = json.dumps(
            message_json,
            sort_keys=True,
            indent=4,
            separators=(',', ': '),
            ensure_ascii=False
        )
    except TypeError:
        json_text = str(message_json)

    return json_text


class ExceptionTemplate(Exception):
    def __init__(self, *args):
        logger.error(self.__class__.__name__)
        super().__init__(*args)


# Selenium #############################################################################################################
# Selenium exception for not start Browser
class SeleniumBrowserNotStarting(ExceptionTemplate):
    pass


# Selenium exception for web driver
class SeleniumWebDriverError(ExceptionTemplate):
    pass


class SeleniumWebElementError(ExceptionTemplate):
    pass


# REST Response ########################################################################################################
# Main exception for REST response
class ResponseException(ExceptionTemplate):
    pass


class RESTConnectionError(ExceptionTemplate):
    def __init__(self, message, response_text='', *args):
        self.message = message

        # Write formatted JSON to stderr
        if type(response_text) in (dict, list):
            # sys.stderr.write(
            #     json.dumps(
            #         response_text,
            #         sort_keys=True,
            #         indent=4,
            #         separators=(',', ': '),
            #         ensure_ascii=False
            #     )
            # )

            response_text = json.dumps(
                response_text,
                sort_keys=True,
                indent=4,
                separators=(',', ': '),
                ensure_ascii=False
            )

        super().__init__(message + '\n' + response_text, *args)


# Test Framework #######################################################################################################
# Main exception for Franchise
class TestFrameworkException(ExceptionTemplate):
    pass


# Objects ##############################################################################################################
# Exceptions for manipulating with objects data
class ObjectDataException(ExceptionTemplate):
    pass


# Exceptions for formatted error
class ObjectDataFormattedException(ExceptionTemplate):
    def __init__(self, message, formatted_output=None, *args):
        self.message = message

        if formatted_output:
            message += '\n' + json_to_stderr(formatted_output)
        super().__init__('\n\n' + message, *args)


# Exception for mismatch error. Args - msg, mismatch_list
class MismatchError(ExceptionTemplate):
    def __init__(self, message, mismatch_list, *args):
        self.message = message
        self.mismatch_list = mismatch_list

        logger.attach_error('JSON', mismatch_list)
        super().__init__('\n\n' + message, *args)

        logger.debug('JSON: \n %s' % json_to_stderr(mismatch_list))


# Exception for .feature steps options
class StepOptionException(ExceptionTemplate):
    pass


# Fail in step
class FailStep(ExceptionTemplate):
    pass


# API formatted exception
class ApiFormattedException(ExceptionTemplate):
    def __init__(self, message, mismatch_list, *args):
        self.message = message

        message += '\n' + json_to_stderr(mismatch_list)
        super().__init__('\n\n' + message, *args)
        logger.debug('JSON: \n %s' % json_to_stderr(mismatch_list))


class AutoRetry(ExceptionTemplate):
    def __init__(self, *args):
        super().__init__(*args)
        logger.critical('Получена неизвестная ошибка!', exc_info=self)

    pass


class XfailError(ExceptionTemplate):
    pass
