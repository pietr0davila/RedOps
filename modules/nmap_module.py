from libraries import subprocess, info, error, error_color, json, xmltodict
from utils.file_utils import file_writer
from utils.tools_utils import is_tool_installed

class NmapModule:
    def __init__(self, type, target):
        self.type = type
        self.target = target

    def show_nmap_scan_in_shell(self):
        if not is_tool_installed(tool="nmap"):
            return
        scanners = {
            1: "-T5 -Pn -sT --top-ports 5000 -vvv",  # Basico: rápido, superficial
            2: "-T5 -Pn -sT --top-ports 10000 -sV -vvv",  # Intermediário: um pouco mais profundo
            3: "-T5 -Pn -sT -p- -A -vvv",  # Avançado: completo, detecta versões, SO e serviços

            -1: "-T3 -Pn --top-ports 5000 -vvv",  # Basico silencioso: mais discreto, menos portas
            -2: "-T2 -Pn --top-ports 10000 -sV -vvv",  # Intermediário silencioso: silencioso, mas com fingerprint leve
            -3: "-T1 -Pn -p- -Sv -O --scan-delay 500ms --max-retries 2 -vvv",  # Avançado silencioso: evasivo e lento, mas completo
            }
        try:

            scanner = scanners.get(self.scan_type)        
            info(f"Nmap scan {scanner} started successfully with args: {scanner}.")
            self.handler_scan_execution(self.target, scanner)
            info("Nmap scan executed successfully.")
        except Exception as e:
            error_color("We found a error while executing nmap feature.")
            error(f"error: {e} running tool 'nmap' ignoring feature.")

    def handler_scan_execution(self, args):
        try:
            info(f"{self.target} {args}")
            self.execute_output_scanning(self.target, args)
        except Exception as e:
            error(f"Nmap scan can't be executed due error: {e}")

    def execute_output_scanning(self, args):
        subprocess.run(["nmap"] + args.split() + [self.target])
        self.save_scan_in_file(self.target, args)

    def save_scan_in_file(self, args):
        xml_result = subprocess.check_output(["nmap", "-oX", "-"] + args.split() + [self.target])
        convert_to_dict = xmltodict.parse(xml_result.decode())
        json_content = json.dumps(convert_to_dict, indent=4)
        file_writer("nmap_data.json", json_content, "NMAP")

