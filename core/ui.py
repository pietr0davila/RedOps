from core.execute import get_execution
from libraries import (
    print, Panel, os, info_color, error_color, warning_color, info, warning, fatal, TERMS_NOT_ACCEPT, USER_INTERRUPTION_ERROR
)


def disclaimer():
    disclaimer_msg = f"""
{info_color('WARNING - LEGAL NOTICE')}
[white]This software was developed strictly for [bold]educational[/bold] and [bold]authorized penetration testing[/bold] purposes.

Using it for unauthorized access, intrusion, or any activity against systems without explicit permission is [bold red]illegal[/bold red] and unethical.

[bold]The developer is NOT responsible for any misuse.[/bold]
Use responsibly and within the boundaries of the law.[/white]
"""
    print(Panel(disclaimer_msg, title=info_color('DISCLAIMER ABOUT USE'), border_style="red"))

    try:
        check = input("[+] Do you agree with the terms? [y/N] ").strip().lower()
        info(f"Accepted terms: {check}")

        if check == "y":
            os.system("cls" if os.name == "nt" else "clear")
            print("[italic green]Welcome![/italic green]\n")
            mode = interactive_menu()
            info(f"Option selected: {mode}")
            get_execution(mode)
        else:
            error_color("Alright... Quitting!")
            fatal("Terms not accepted, exiting.", TERMS_NOT_ACCEPT)

    except KeyboardInterrupt:
        error_color("\nInput interrupted... Quitting!")
        fatal("Execution interrupted by user.", USER_INTERRUPTION_ERROR)


def interactive_menu():
    print(info_color("Use schema: mysite.com in URLs"))
    print("[italic purple]Reminder: Choosing one option will execute all its steps![/italic purple]\n")
    print("[1] Enumeration - Use scan results to get version and banners")
    print("[2] Exploitation - Search for vulnerabilities in active services")
    print("[3] Post-exploitation - Gather information after gaining access")

    while True:
        try:
            mode = int(input("> "))
            if 1 <= mode <= 3:
                info(f"Valid mode selected: {mode}")
                return mode
            else:
                error_color("Please enter a number between 1 and 3.")
                warning("Input out of range.")
        except ValueError:
            error_color("Invalid input. Please enter a valid number.")
            warning("Numbers only.")
        except KeyboardInterrupt:
            error_color("\nInput interrupted... Quitting!")
            fatal("KeyboardInterrupt: exiting.", USER_INTERRUPTION_ERROR)


def scan_user_interface():
    info_color("""
[1] Basic Scan        - Fast scan on top 5,000 ports, limited details
[2] Intermediary Scan - Broader scan on 10,000 ports, moderate detail
[3] Advanced Scan     - Full scan on all 65,535 ports, detailed report

Add '-' before the number to run in silent mode (firewall evasion).
Ex. -2 will Execute intermediary scan with silent arguments
See full guide in RedOps/README.md
""")
    print("[+] Select scan mode:")
    try:
        while True:
            try:
                mode = int(input("> "))
                return mode
            except ValueError:
                warning("Numbers only")
                warning_color("Please enter a valid scan type")
    except KeyboardInterrupt:
        fatal("Keyboard interruption: Quiting", USER_INTERRUPTION_ERROR)