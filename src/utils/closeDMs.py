import requests
from utils.common import *

def close_all_dms(token):
    set_console_title("Chronos V1 | Made by maxツ#8355 | Close DMs")
    headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
    for channel in close_dm_request:
        print(f"[ {Fore.LIGHTCYAN_EX}C{Fore.RESET} ] {Fore.LIGHTCYAN_EX}ID: "+channel['id'] + Fore.RESET)
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}",
            headers=headers,)