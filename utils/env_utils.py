import os
from dotenv import load_dotenv

def get_env(key_name):
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    dotenv_path = os.path.join(root_path, ".env")
    load_dotenv(dotenv_path=dotenv_path)
    return os.getenv(key_name)