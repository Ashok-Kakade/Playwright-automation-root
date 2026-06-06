import logging

class Logger:
    def get_logger(self):
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger()
    
    