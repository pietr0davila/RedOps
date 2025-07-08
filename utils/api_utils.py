from codes import API_EXCEPTION
from utils.ui_utils import error_color
from utils.env_utils import get_env
import shodan, sys

def shodan_api():
    SHODAN_KEY = get_env("SHODAN_KEY")
    api = shodan.Shodan(SHODAN_KEY)
    try:
        pass
    except shodan.APIError as error:
        error_color(f"We found a error with shodan recognition\n{error}")
        sys.exit(API_EXCEPTION)