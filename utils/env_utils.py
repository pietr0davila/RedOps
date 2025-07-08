import os
from dotenv import load_dotenv

def get_env(key_name: str):
    load_dotenv()
    return os.getenv(key_name)