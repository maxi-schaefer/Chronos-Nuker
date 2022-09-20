import time
import requests
from colorama import Fore



def hypeSquadChanger():
    hypetoken = input(f"Token: {Fore.RESET}")
    print(f"\n[1] Bravery\n[2] Briliance\n[3] Balance\n")
    hypesquad = input(f"Choice: {Fore.RESET}")
    headersosat = {
        'Authorization': str(hypetoken)
    }

    payloadsosat = {
        'house_id': str(hypesquad)
    }
    time.sleep(1)
    rep = requests.session().post("https://discord.com/api/v8/hypesquad/online", json=payloadsosat, headers=headersosat)