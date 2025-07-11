from libraries import (
    shutil, os, subprocess, info, warning, error, info_color, warning_color, error_color, success_color
    )
  
def is_tool_installed(tool):
    if os.name != "nt":
        if shutil.which(tool) is None:
            info_color(f"[*] {tool} not found in the system. Trying to install...")
            warning(f"{tool} not found. The program will attempt to install it.")
            try:
                info("Trying to install via apt repository.")
                subprocess.run(["sudo", "apt", "install", "-y", tool], check=True)
                success_color("Installed successfully via apt.")
                info(f"Tool '{tool}' installed via apt.")  
                return True
            except subprocess.CalledProcessError:
                warning("Apt not available on this host.")
                warning_color("Apt not available on this host.")
                info("Trying to install via snap repository.")
                info_color("[*] Trying with snap repository...")
                try:
                    subprocess.run(["sudo", "snap", "install", tool], check=True)
                    success_color("Installed successfully via snap.")
                    info(f"Tool {tool} installed successfully via snap.")
                    return True
                except subprocess.CalledProcessError:
                    error("Snap not available on this host. Please install Nmap manually from https://nmap.org/download/")
                    error_color(f"Snap not found. See RedOps/logs/RedOps.log. Ignoring {tool} for this script.")
        else:
            info(f"{tool} already installed.")
            return True
    else:
        # ADICIONAR A COMPATIBILIDADE COM WINDOWS
        # VERIFICAR SE NMAP EXISTE COM WHERE
        # SE NÃO EXISTIR INSTALA VIA WGET OU CURL
        # EXECUTA O NMAP        
        return False
