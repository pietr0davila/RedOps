from libraries import print
from utils.logger_utils import setup_logger

logger = setup_logger()

def success_color(msg):
    print(f"[green bold][+]{msg}[/green bold]")

def info_color(msg):
    print(f"[white bold]{msg}[/white bold]")

def warning_color(msg):
    print(f"[yellow bold][-]{msg}[/yellow bold]")

def error_color(msg):
    print(f"[red bold][-]{msg}[/red bold]")