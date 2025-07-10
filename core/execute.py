from libraries import *
from core.get_functions import *
from codes import ERROR_PROCESSING_EXECUTION
from utils.ui_utils import error_color
from utils.target_utils import get_target

def get_execution(choosed):
    target = get_target()
    # Pega as funções que vão ser executadas (de acordo com o que o usuário escolheu no menu)
    options = {
        1: enumeration,
        2: exploiting,
        3: post_exploit,
    }
    if choosed > 1 and choosed <= 3:
        
        for i in range(1, choosed + 1):
            function = options.get(i)       
            if function is not None:
                
                function(target)
            else:
                error_color("We encountered an error processing your request... Quiting!")
                sys.exit(ERROR_PROCESSING_EXECUTION)
    else:
        error_color("You entered a invalid option... Quiting!")
        sys.exit()