# Bibliotecas padrão py3

import sys
import os
import logging
import ipaddress
import socket
import subprocess
import shutil
import getpass
import json

# Bibliotecas externas
import nmap
import xmltodict
from logging.handlers import RotatingFileHandler
from rich import print
from rich.panel import Panel

# Utilitários
from utils.logger_utils import (
    fatal, 
    info, 
    warning,
    debug,
    error
)
from utils.ui_utils import (
    error_color,
    info_color,
    success_color,
    warning_color
)
# Códigos de erro
from codes import (
    TERMS_NOT_ACCEPT,
    USER_INTERRUPTION_ERROR,
    INVALID_INPUT,
    ERROR_PROCESSING_EXECUTION,
    TARGET_UNREACHABLE,
    ERROR_INSTALLING_NMAP,
    PERMISSION_DENIED,
)