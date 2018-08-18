import logging

# Log format codes
# %(asctime)s             Time when the log was created.
# %(created)f             Return from time.time().
# %(filename)s            Filename.
# %(funcName)s            Name of the function.
# %(levelname)s           Logging level for the message.
# %(levelno)s             Numeric logging level.
# %(lineno)d              Line in the file where the logging call exists.
# %(message)s             The logged message.
# %(module)s              Module.
# %(msecs)d               Millisecond portion of the time when the log was created.
# %(name)s                Name of the logger used to log the call.
# %(pathname)s            Full pathname of the source file where the logging call was issued.
# %(process)d             Process ID.
# %(processName)s         Process name.
# %(relativeCreated)d     Time, in milliseconds, when the log was created.
# %(thread)d              Thread ID.
# %(threadName)s          Thread name.

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno == logging.CRITICAL:
            record.levelname = (f"\033[38;5;255;1m\033[41;1m   {record.levelname} \033[0m")
        elif record.levelno == logging.ERROR:
            record.levelname = f"\033[91;1m\033[40m    {record.levelname}   \033[0m"
        elif record.levelno == logging.WARNING:
            record.levelname = f"\033[93;1m\033[40m   {record.levelname}  \033[0m"
        elif record.levelno == logging.INFO:
            record.levelname = f"\033[38;5;255;1m\033[42m     OK     \033[0m"
        elif record.levelno == logging.DEBUG:
            record.levelname = (f"\033[38;5;255;1m\033[44m    {record.levelname}   \033[0m")
        return logging.Formatter.format(self, record)


logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()

log_format = "[%(levelname)s] %(asctime)s - \033[38;5;254m\033[40m%(message)s (\033[38;1m\033[40m%(filename)s:%(funcName)s:\033[31;1m%(lineno)s\033[0m\033[38;5;255m)\033[0m"
time_format = "\033[38;5;245m\033[40m" + "%H:%M:%S" + "\033[0m"
formatter = ColoredFormatter(log_format, datefmt=time_format)
handler.setFormatter(formatter)
logger.addHandler(handler)

if __name__ == "__main__":
    logger.critical("this is crit")
    logger.error("this is err")
    logger.warning("this is warn")
    logger.info("this is nfo")
    logger.debug("this is dbug")
