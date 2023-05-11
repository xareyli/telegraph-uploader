import requests
import json


def createAccount(short_name, author_name):
    """Create a new user account on https://telegra.ph/

    Creates an account with given credentials and returns servers response, False if couldn't create an account

    """
    if not isinstance(short_name, str):
        raise TypeError('short_name must be a string')
    if not isinstance(author_name, str):
        raise TypeError('author_name must be a string')

    account = requests.post('https://api.telegra.ph/createAccount?short_name={}&author_name={}'.format(short_name, author_name))

    resp_decoded = json.loads(account.content.decode())

    if resp_decoded['ok'] == True and str(account.status_code).startswith('2'):
        return account.json()['result']
    else:
        return False
