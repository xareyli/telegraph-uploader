import requests
import json


def createAccount(short_name, author_name):
    """Create a new user account on https://telegra.ph/

    Creates an account with given credentials and returns servers response, False if couldn't create an account

    """
    account = requests.post('https://api.telegra.ph/createAccount?short_name={}&author_name={}'.format(short_name, author_name))

    resp_decoded = json.loads(account.content.decode())

    if not resp_decoded['ok'] or not str(account.status_code).startswith('2'):
        return account.json()['result']
    else:
        return False
