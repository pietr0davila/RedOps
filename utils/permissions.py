from libraries import os, sys, getpass, PERMISSION_DENIED, fatal, error_color
from utils.system_utils import check_if_is_unix

def execute_as_sudo():
    if check_if_is_unix():
        if os.geteuid() != 0:
            error_color("RedOps must be run as root, trying run with sudo...")
            try:
                os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
                return True
            except PermissionError:
                error_color("You don't have sufficient permissions for this script")
                fatal(f"Insufficient permissions, user {getpass.getuser} can't execute program as sudo. change sudoers rules or execute as root", PERMISSION_DENIED)
                return False
    else:
        return "nt"