from utils.ui_utils import *
from libraries import print, Panel
import os
import sys
from codes import TERMS_NOT_ACCEPT, USER_INTERRUPTION_ERROR
from core.execute import get_execution

def disclaimer(logger=None):
    disclaimer_msg = f"""
{info_color('WARNING - LEGAL NOTICE')}
[white]This software was developed strictly for [bold]educational[/bold] and [bold]authorized penetration testing[/bold] purposes.\n
Using it for unauthorized access, intrusion, or any activity against systems that you don't have explicit permission to test [bold red]is illegal[/bold red] and unethical.\n\n
[bold]The developer is NOT responsible for any misuse.[/bold]\n
Use responsibly and within the boundaries of the law.[/white]) """
    print(Panel(disclaimer_msg, title=f"{info_color('DISCLAIMER ABOUT USE')}", border_style="red"))
    try:
        check = input("[+] Did you agree with the terms? [y/N] ")
        if logger:
            logger.info(f"Accepted terms: {check}")
        if check == "y" or check == "Y":
            os.system("cls" if os.name == "nt" else "clear")
            print("[italic green]Welcome! [/italic green]\n")
            mode = interactive_menu(logger)
            if logger:
                logger.info(f"Option selected: {mode}")
            get_execution(mode)
        else:
            error_color("All right... Quiting!")        
            if logger:
                logger.warning("Terms not accepted, exiting")
            sys.exit(TERMS_NOT_ACCEPT)
    except KeyboardInterrupt:
        error_color("\nInput has been interrupted... Quiting!")
        if logger:
            logger.error("Execução interrompida pelo usuário.")

def interactive_menu(logger=None):
    print(f"{info_color('Use schema mysite.com in URLs')}")
    print("[italic purple]Remember, if you choose one option, all numbers  wi'll be executed!! [/italic purple]\n\n")
    print("[1] Enumeration - Use scan results to get version and banners")
    print("[2] Exploitation - Search for vulnerabilities in active services")
    print("[3] Post-exploitation - Gather information after gaining access")
    # Validação robusta de entrada
    while True:
        try:
            mode = int(input("> "))
            if 1 >= mode and mode <= 3:
                return mode
            else:
                error_color("Please enter a number between 1 and 3.")
                if logger:
                    logger.warning("Entry out of range.")
        except ValueError:
            error_color("Invalid input. Please enter a valid number.")
            if logger:
                logger.warning("Insert only numbers!")
        except KeyboardInterrupt:
            error_color("\nInput has been interrupted... Quiting!")
            if logger:
                logger.error("Keyboard Interrupt error... Quiting")
            sys.exit(USER_INTERRUPTION_ERROR)

