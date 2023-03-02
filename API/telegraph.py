import requests
import os


class Telegraph:
    def createAccount(self, short_name, author_name):
        account = requests.post('https://api.telegra.ph/createAccount?short_name={}&author_name={}'.format(short_name, author_name)).text

        return account

    def upload(self, access_token, imgDir):
        html_content = ""

        with os.scandir(imgDir) as entries:
            for entry in entries:
                fullPath = '{}/{}'.format(imgDir, entry.name)

                # TODO
