import requests
from termcolor import colored


def print_ip(ip):
    if ip['cc'] != 'US':
        ip_address = colored(ip['ip'], 'green')
        country = colored(ip['country'], 'green')
        cc = colored(ip['cc'], 'green')
    else:
        ip_address = colored(ip['ip'], 'blue')
        country = colored(ip['country'], 'blue')
        cc = colored(ip['cc'], 'blue')

    print(f"Public IP Address: {ip_address}")
    print(f"Country: {country}")
    print(f"CC: {cc}")


ip = requests.get('https://api.myip.com').json()

print_ip(ip)
