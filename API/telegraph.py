import requests
import os
from utils import scaleImage
import logging
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import json


class Telegraph:
    def createAccount(self, short_name, author_name):
        logging.info('API: creating new account')

        try:
            account = requests.post('https://api.telegra.ph/createAccount?short_name={}&author_name={}'.format(short_name, author_name))

            resp_decoded = json.loads(account.content.decode())

            if not resp_decoded['ok']:
                raise Exception(resp_decoded['error'])

            if not str(account.status_code).startswith('2'):
                raise HTTPError('API: response code differs from 2xx')

            logging.info('API: account created successfuly')

            return account.json()['result']
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError, Exception) as e:
            logging.error('[ERROR]: ' + str(e))
            return False

    def upload(self, access_token, imgDir):
        html_content = ""

        for path,subdir,files in os.walk(imgDir):
            for name in files:
                fullpath = os.path.join(path,name)

                print('Original image size {} Mb'.format(os.stat(fullpath).st_size / (1024 * 1024)))
                print('Scaled image size {} Mb'.format(os.stat(scaleImage(fullpath)).st_size / (1024 * 1024)))
                print('------------------------------------------------------')
