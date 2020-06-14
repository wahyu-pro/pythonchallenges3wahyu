import logging
class Log:
    @staticmethod
    def main():
        # # create logger
        # logger = logging.getLogger("logging_tryout2")
        # logger.setLevel(logging.DEBUG)
        # # create console handler and set level to debug
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.DEBUG)

        # # create formatter
        # formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")

        # # add formatter to ch
        # ch.setFormatter(formatter)

        # # add ch to logger
        # logger.addHandler(ch)

        # logging.basicConfig(filename="file.log", filemode='w')

        # # "application" code
        # logger.debug("debug message")
        # logger.info("info message")
        # logger.warn("warn message")
        # logger.error("error message")
        # logger.critical("critical message")
        fmtstr = "%(asctime)s: (%(filename)s): %(levelname)s: %(funcName)s Line: %(lineno)d - %(message)s"
        datestr = "%Y-%m-%d %H:%M:%S"
        #basic logging config
        logging.basicConfig(
            filename="custom_log_output.log",
            level=logging.DEBUG,
            filemode="w",
            format=fmtstr,
            datefmt=datestr,
        )
        logging.info("This is an information about something")
        logging.error("We can't divide any numbers by zero")
        # logging.notice("Someone loves your status")
        logging.warning("Insufficient funds.")
        logging.debug("This is debug message.")
        logging.critical("Medic!! We've got critical damages.")
        # logging.emergency("System hung. Contact system administrator immediately!")

Log.main()