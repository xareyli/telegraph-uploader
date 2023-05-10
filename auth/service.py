from libs.telegraph import createAccount
from store import store
import logging


class AuthWindowService:
    def registerUser(self, short_name, author_name):
        logging.info('API: creating new account')
        account = createAccount(short_name, author_name)

        if not account:
            return False

        store.dset('API', 'access_token', account['access_token'])

        logging.info('API: account created successfuly')

        return account['auth_url']
