import logging
import os

def setup_logger():
    log_file = "RedOps.log"
    log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../logs"))
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_file)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        filename=log_path
    )
    return logging.getLogger('RedOps')
