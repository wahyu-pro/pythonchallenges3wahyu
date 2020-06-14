import logging
class Log:
    @staticmethod
    def main():
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