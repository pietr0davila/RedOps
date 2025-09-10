from modules.nmap_module import NmapModule

def enumeration(target):
    from core.ui import scan_user_interface
    mode = scan_user_interface()
    NmapModule(target, mode).show_nmap_scan_in_shell() 
