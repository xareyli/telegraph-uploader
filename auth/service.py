from API.telegraph import Telegraph
from store import store


class AuthWindowService:
    def __init__(self):
        self.telegraph = Telegraph()

    def registerUser(self, short_name, author_name):
        account = self.telegraph.createAccount(short_name, author_name)

        if not account:
            return False

        store.dset('API', 'access_token', account['access_token'])

        return account['auth_url']
