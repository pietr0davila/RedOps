from core.phases import *
from core.target import get_target
from libraries import (
    sys, error_color, ERROR_PROCESSING_EXECUTION,
    INVALID_INPUT, fatal, success_color
)

def get_execution(choosed):
    target = get_target()

    options = {
        1: enumeration,
        2: exploiting,
        3: post_exploit,
    }

    if 1 <= choosed <= 3:
        for i in range(1, choosed + 1):
            function = options.get(i)
            if function:
                success_color(f"Starting phase {i}")
                function(target)
            else:
                error_color("An error occurred while processing your request... Quitting!")
                fatal("Error processing request. exiting", ERROR_PROCESSING_EXECUTION)
    else:
        error_color("Invalid option selected... Quitting!")
        fatal("Invalid input provided.", INVALID_INPUT)
