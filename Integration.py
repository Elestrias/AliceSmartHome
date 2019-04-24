import requests
from app import SMARTHOMESERVER_ERROR

def check_password(webhook_url, password):
    try:
        r = requests.get(webhook_url, params={'password': password}).json()
        return r['ok']
    except Exception:
        return SMARTHOMESERVER_ERROR
