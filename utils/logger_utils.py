from libraries import os, logging, sys,RotatingFileHandler
from modules.logger_module import setup_logger

logger = setup_logger()

def info(msg):
    logger.info(msg)

def warning(msg):
    logger.warning(msg)

def error(msg):
    logger.error(msg)

def fatal(msg, code):
    logger.fatal(msg)
    sys.exit(code)

def debug(msg):
    # FUNÇÃO EXCLUSIVA NO DEBUGGING!!
    logger.debug(msg)
