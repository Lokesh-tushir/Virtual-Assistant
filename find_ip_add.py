import requests


def find_ip_add():
    ip_address = requests.get('https://api64.ipify.org?format=json').json
    return ip_address["ip"]
