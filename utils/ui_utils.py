from libraries import print

def success_color(msg):
    print(f"[green bold][+]{msg}[/green bold]")

def info_color(msg):
    print(f"[white bold]{msg}[/white bold]")

def warning_color(msg):
    print(f"[yellow bold][-]{msg}[/yellow bold]")

def error_color(msg):
    print(f"[red bold][-]{msg}[/red bold]")