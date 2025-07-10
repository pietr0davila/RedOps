from utils.logger_utils import info, warning, error, fatal
from libraries import ipaddress, socket, subprocess, os, ERROR_GETTING_TARGET

def get_target():
    while True:
        try:
            print("[+] What's your target?")
            target = input("> ")
            if any([is_host(target), is_ip_or_network(target), ping_host(target)]):
                info("Target successfully validated")
                return target
        except ValueError or KeyboardInterrupt:
            error("Invalid input, trying again...")       
            continue

def ping_host(target):
    param = "-n" if os.name == "nt" else "c"
    command = [
        "ping",
        param, 
        "1",
        target
    ]
    info("Executing ping test in target %s" + target)
    return subprocess.run(command,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
def is_host(target):
    try:
        socket.gethostbyname(target)
        info("Search for host name: %s" + target)
        return True
    except ValueError:
        warning("Target is not a hostname")
        return False

def is_ip_or_network(target):
    try:
        ipaddress.ip_address(target)
        info("Checking if target is IP address")
        return True
    except ValueError:
        try:
            warning("Target is not a IP address") 
            info("Checking if target is a IP network")
            ipaddress.ip_network(target, strict=False)
            return True
        except ValueError:
            fatal("It was not possible to check target origin", ERROR_GETTING_TARGET)
            return False