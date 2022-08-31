import logging

from datetime import datetime

# logging config
logging.basicConfig(
    filename="log_output.log",
    level=logging.DEBUG,
    filemode="a",
)


# to add info log to logging
def logInfo(file_name, function_name, log_message):
    now = datetime.now()
    dt_string = now.strftime('%Y-%m-%d %H:%M:%S.%p')
    logging.info(
        dt_string + "  File : " + file_name + "  Function : " + function_name + "  Message: " + log_message)


# to add error log to logging
def logError(file_name, function_name, log_message, log_error):
    now = datetime.now()
    dt_string = now.strftime('%Y-%m-%d %H:%M:%S.%p')
    logging.error(
        dt_string + "  File : " + file_name + "  Function : " + function_name + "  Message: " + log_message + "  Error : " + log_error)
