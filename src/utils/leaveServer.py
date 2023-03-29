import requests
from utils.common import *

def leaveServer(token):
    set_console_title("Chronos V1 | Made by maxツ#8355 | Leave Server")
    headers = {'Authorization': token}
    guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], headers={'Authorization': token})
            print(f"[ {Fore.LIGHTCYAN_EX}C{Fore.RESET} ] {Fore.LIGHTCYAN_EX}Left Server: "+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")