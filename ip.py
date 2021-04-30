#!/usr/bin/python3

import argparse
import sys

import requests
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--city",
                    dest="home_city",
                    help="Set home city",
                    action='store')
args = parser.parse_args()
home_city = args.home_city if args.home_city else None


def get_ip(response):
    """get_ip.

    :param response:
    """
    return response['ip']


def print_location(geo_response, city, ip_address):
    """print_location.

    :param geo_response:
    :param city:
    :param ip_address:
    """
    if geo_response['city'].lower() == city.lower():
        print(colored('------------------------', 'red'))
        print(colored('[*] NOT Connected to VPN', 'red'))
        print(colored('------------------------', 'red'))
        print('IP Address: ', colored(ip_address, 'red'))
        print('Country: ', colored(geo_response['country'], 'red'))
        print('Region Name: ', colored(geo_response['regionName'], 'red'))
        print('City: ', colored(geo_response['city'], 'red'))
        print('ISP: ', colored(geo_response['isp'], 'red'))
        print('Org: ', colored(geo_response['org'], 'red'))
    else:
        print(colored('--------------------', 'green'))
        print(colored('[.] Connected to VPN', 'green'))
        print(colored('--------------------', 'green'))
        print('IP Address: ', colored(ip_address, 'green'))
        print('Country: ', colored(geo_response['country'], 'green'))
        print('Region Name: ', colored(geo_response['regionName'], 'green'))
        print('City: ', colored(geo_response['city'], 'green'))
        print('ISP: ', colored(geo_response['isp'], 'green'))
        print('Org: ', colored(geo_response['org'], 'green'))


def main(home_city=home_city):
    """main.

    :param home_city:
    """
    if not home_city:
        print(parser.print_help())
        sys.exit('[!] Please provide a city\n')

    ip_response = requests.get('https://api.myip.com').json()

    ip_address = get_ip(ip_response)

    geo_response = requests.get('http://ip-api.com/json/{}'.format
                                (ip_address)).json()

    print_location(geo_response, home_city, ip_address)


if __name__ == '__main__':
    main(home_city=home_city)
