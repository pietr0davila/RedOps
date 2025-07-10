from libraries import os, shutil, subprocess, nmap
from utils.logger_utils import info, error, warning
from utils.ui_utils import *

def is_nmap_installed():
    if os.name != "nt":
        if shutil.which("nmap") is None:
            info_color("[*] Nmap not found in the system. Trying to install...")
            warning("Nmap not found. The program will attempt to install it.")
            try:
                info("Trying to install via apt repository.")
                subprocess.run(["sudo", "apt", "install", "-y", "nmap"], check=True)
                success_color("Installed successfully via apt.")
                info("Tool 'nmap' installed via apt.")  
                return True
            except subprocess.CalledProcessError:
                warning("Apt not available on this host.")
                warning_color("Apt not available on this host.")
                info("Trying to install via snap repository.")
                info_color("[*] Trying with snap repository...")
                try:
                    subprocess.run(["sudo", "snap", "install", "nmap"], check=True)
                    success_color("Installed successfully via snap.")
                    info("Tool 'nmap' installed successfully via snap.")
                except subprocess.CalledProcessError:
                    error("Snap not available on this host. Please install Nmap manually from https://nmap.org/download/")
                    error_color("Snap not found. See RedOps/logs/RedOps.log. Ignoring Nmap for this script.")
        else:
            info("Nmap already installed.")
            return True
    else:
        # ADICIONAR A COMPATIBILIDADE COM WINDOWS
        # VERIFICAR SE NMAP EXISTE COM WHERE
        # SE NÃO EXISTIR INSTALA VIA WGET OU CURL
        # EXECUTA O NMAP        
        return False

def nmap_scanning(target, scan_type):
    is_nmap_installed()
    try:
        scanner = nmap.PortScanner()
        logger = setup_logger()
        if scan_type.startswith("-"):
            silent_args = "-sS -Pn --max-retries 1 --min-rate 10 -f -D RND:10"
            # Modo de evasão (silent)
            # Não completa o 3-way handshake
            # Não envia o ping para o host (Assume up)
            # Velocidade mais lenta
            # Tenta cada porta uma vez ou sai
            # Baixa frequência de pacotes
            # Fragmenta pacotes para evitar a inspeção do firewall
            # Spoof de IP, envia 10 IPs falsos como "distração"
            if scan_type == 1:
                try:
                    scanner.scan(target, arguments=f"-T2 --top-ports 10000 {silent_args}")
                    logger.info("Nmap silent basic scan started successfully.")
                except Exception as e:
                    error_color("Error with basic silent scan")
                    error(f"Error with scan: {e}")
        # Scan avançado, ignora ping, velocidade T4 e escaneia as 65k portas
        #        scanner.scan(target, arguments="-A -Pn -T4 -p- -vvv")
        logger.info("Nmap scan executed successfully.")
    except PermissionError:
        error_color("You don't have sufficient permissions to run this script.")
        error("Permission denied while attempting to run Nmap.")
