from libraries import os, sys, getpass, PERMISSION_DENIED, fatal, error_color


def execute_as_sudo():
    if os.geteuid() != 0:
        error_color("RedOps must be run as root, trying rerun with sudo...")
        try:
            os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
            return True
        except PermissionError:
            error_color("You don't have sufficient permissions for this script")
            fatal(f"Insufficient permissions, user {getpass.getuser} can't execute program as sudo. change sudoers rules or execute as root", PERMISSION_DENIED)
            return False