from libraries import os, logging, sys
from libraries import RotatingFileHandler


def setup_logger():
    log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../logs"))
    log_file = "RedOps.log"
    log_path = os.path.join(log_dir, log_file)
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger("RedOps")
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        handler = RotatingFileHandler(log_path, maxBytes=5_000_000, backupCount=3)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        logger.info("Logger running in: %s" + log_path)
    else:
        logger.info("Logger configured successfully.")

    return logger

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
