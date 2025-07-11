from modules.nmap_module import show_nmap_scan_in_shell

def enumeration(target):
    from core.ui import scan_user_interface
    mode = scan_user_interface()
    show_nmap_scan_in_shell(target, mode) 
