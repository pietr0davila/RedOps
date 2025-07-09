from libraries import *
from codes import TERMS_NOT_ACCEPT 
from core.ui import disclaimer
from utils.logger_utils import setup_logger

def main():
    logger = setup_logger()
    logger.info('RedOps started.')
    disclaimer(logger)

if __name__ == "__main__":
    main()