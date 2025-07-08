from utils.ui_utils import error_color
from libraries import *
from codes import TERMS_NOT_ACCEPT
from core.execute import get_execution

def disclaimer():
    disclaimer_msg = """
[bold yellow]  WARNING - LEGAL NOTICE[/bold yellow]
[white]This software was developed strictly for [bold]educational[/bold] and [bold]authorized penetration testing[/bold] purposes.\n
Using it for unauthorized access, intrusion, or any activity against systems that you don't have explicit permission to test [bold red]is illegal[/bold red] and unethical.\n\n
[bold]The developer is NOT responsible for any misuse.[/bold]\n
Use responsibly and within the boundaries of the law.[/white]) """
    print(Panel(disclaimer_msg, title="[bold yellow] DISCLAIMER ABOUT USE [/ bold yellow]", border_style="red"))
    try:
        check = input("[+] Did you agree with the terms? [y/N] ")
        if check == "y" or check == "Y":
            os.system("clear") if os.name != "nt" else os.system("cls")
            print("[italic green]Welcome! [/ italic green]\n")
            mode = interactive_menu()
            get_execution(mode)
        else:
            error_color("All right... Quiting!")        
            sys.exit(TERMS_NOT_ACCEPT)
    except KeyboardInterrupt:
        error_color("\nInput has been interrupted... Quiting!")

def interactive_menu():
    print("[italic purple]Remember, if you choose 4, numbers 1, 2, 3 and 4 wi'll be executed!! [/italic purple]\n\n")
    print("[1] Network reconnaissance - No direct interaction with the target")
    print("[2] Scanning - Get open ports, active hosts and enable services")
    print("[3] Enumeration - Use scan results to get version and banners")
    print("[4] Exploitation - Search for vulnerabilities in active services")
    print("[5] Brute force - Exploit inputs with multiple attempts")
    print("[6] Post-exploitation - Gather information after gaining access")
    # Executa a varredura de tudo até chegar no número digitado
    mode = int(input("> "))
    return mode

