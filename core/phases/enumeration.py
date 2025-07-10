from utils.nmap_utils import nmap_scanning    

def enumeration(target):
    print("""
    [1] Basic Scan - Basic config scanning, ready in seconds but less reports in 5000 most common ports
    [2] Intermediary Scan - Intermediary config scanning, ready in seconds or a few minutes in 10000 ports 
    [3] Advanced Scan - Advanced Scanning, complete report but takes longer, scan all 65k ports
    "-"+<number> Execute silent scan, with firewall bypass
    Details in RedOps/README.md
        """)
    print("[+] Select mode for recognition")
    mode = int(input("> "))
    nmap_scanning(target, mode) 
