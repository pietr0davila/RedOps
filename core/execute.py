from libraries import *
from codes import ERROR_PROCESSING_EXECUTION
from core.get_functions import *
from utils.ui_utils import error_color

def get_execution(choosed):
    # Get all function that wi'll be executed
    options = {
        1: enumeration,
        2: exploiting,
        3: post_exploit,
    }
    if choosed > 1 and choosed <= 3:
        for i in range(1, choosed + 1):
            function = options.get(i)       
            if function is not None:
                function()
            else:
                error_color("We encountered an error processing your request... Quiting!")
                sys.exit(ERROR_PROCESSING_EXECUTION)
    elif choosed == 1:
        function = options.get(choosed)
        if function is not None:
            function()
    else:
        error_color("You entered a invalid option... Quiting!")
        sys.exit()