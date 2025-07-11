from libraries import (
    ipaddress, socket, subprocess, os,
    TARGET_UNREACHABLE, info, warning, fatal,
    error_color, success_color
)

def get_target():
    while True:
        print("[+] Enter the target (IP, hostname or network):")
        target = input("> ").strip()
        
        success_msg = "Target successfully validated."
        is_ip = is_ip_or_network(target)
        is_hostname = is_host(target)
        is_reachable = ping_host(target)

        if is_ip:
            info(f"{target} is a valid IP address or network.")
            success_color(success_color)
            return target

        elif is_hostname:
            info(f"{target} is a valid hostname.")
            success_color(success_color)
            return target

        elif is_reachable:
            info(f"{target} responded to ping.")
            success_color(success_color)
            return target

        else:
            error_color(f"Target '{target}' is unreachable or invalid.")
            fatal("Target unreachable or invalid.", TARGET_UNREACHABLE)


def ping_host(target):
    param = "-n" if os.name == "nt" else "-c"
    command = ["ping", param, "1", target]
    info(f"Executing ping test on target: {target}")
    
    return subprocess.run(
        command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    ).returncode == 0


def is_host(target):
    try:
        ip = socket.gethostbyname(target)
        info(f"Resolved hostname {target} to {ip}")
        return True
    except socket.gaierror:
        warning("Target is not a resolvable hostname.")
        return False


def is_ip_or_network(target):
    try:
        ip = ipaddress.ip_address(target)
        info(f"Valid IP address: {ip} (version: {ip.version})")
        return True
    except ValueError:
        warning("Target is not a valid IP address.")
        try:
            network = ipaddress.ip_network(target, strict=False)
            info(f"Valid IP network: {network}")
            return True
        except ValueError:
            warning(f"Target '{target}' is not a valid IP network.")
            return False
