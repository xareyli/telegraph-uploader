import requests
import os
from utils import scaleImage


class Telegraph:
    def createAccount(self, short_name, author_name):
        account = requests.post('https://api.telegra.ph/createAccount?short_name={}&author_name={}'.format(short_name, author_name)).text

        return account

    def upload(self, access_token, imgDir):
        html_content = ""

        for path,subdir,files in os.walk(imgDir):
            for name in files:
                fullpath = os.path.join(path,name)

                print('Original image size {} Mb'.format(os.stat(fullpath).st_size / (1024 * 1024)))
                print('Scaled image size {} Mb'.format(os.stat(scaleImage(fullpath)).st_size / (1024 * 1024)))
                print('------------------------------------------------------')
