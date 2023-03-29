import requests
from utils.common import *

def tokenInfo(token):
    set_console_title("Chronos V1 | Made by maxツ#8355 | Token Info")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
[{Fore.LIGHTCYAN_EX}User ID{Fore.RESET}]         {userID}
[{Fore.LIGHTCYAN_EX}User Name{Fore.RESET}]       {userName}
[{Fore.LIGHTCYAN_EX}2 Factor{Fore.RESET}]        {mfa}
[{Fore.LIGHTCYAN_EX}Email{Fore.RESET}]           {email}
[{Fore.LIGHTCYAN_EX}Phone number{Fore.RESET}]    {phone if phone else "None"}
[{Fore.LIGHTCYAN_EX}Token{Fore.RESET}]           {token}
            ''')
            input('Press any key to continue...')