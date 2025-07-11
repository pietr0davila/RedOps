from core.ui import disclaimer
from utils.permissions import execute_as_sudo
from libraries import info

def main():
    execute_as_sudo()
    info('RedOps started.')
    disclaimer()

if __name__ == "__main__":
    main()