import os

def check_if_is_unix():
    if os.name == "posix":
        return True
    return False