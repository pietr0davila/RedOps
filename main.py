from libraries import *
from codes import TERMS_NOT_ACCEPT 
from core.ui import disclaimer
from utils.logger_utils import setup_logger
from utils.ui_utils import error_color
def execute_as_sudo():
    if os.geteuid() != 0:
        error_color("RedOps must be run as root, trying rerun with sudo...")
        os.execvp("sudo", ["sudo", sys.executable] + sys.argv)

def main():
    execute_as_sudo()
    logger = setup_logger()
    logger.info('RedOps started.')
    disclaimer(logger)

if __name__ == "__main__":
    main()