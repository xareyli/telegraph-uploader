import requests
import os
from utils import scaleImage, getImageExtension, html_to_nodes
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
                is_resized = False
                fullpath = os.path.join(path,name)

                # if the image is more than 5 Mb, resize it
                if os.stat(fullpath).st_size / (1024 * 1024) > 5:
                    fullpath = scaleImage(fullpath)
                    is_resized = True

                with open(fullpath, 'rb') as imageF:
                    image_extension = getImageExtension(fullpath)

                    response = requests.post(
                        'https://telegra.ph/upload',
                        files={'file': ('file', imageF, 'image/{}'.format(image_extension))}
                    )

                    image_uploaded = json.loads(response.text)

                    if not ('error' in image_uploaded):
                        src = image_uploaded[0]['src']

                        html_content = html_content + "<img src='{}' />".format(src)
                    else:
                        logging.warning('[API]: skipped "{}" due to "{}"'.format(fullpath, image_uploaded['error']))

                # remove thumbnail
                if is_resized:
                    os.remove(fullpath)

        content_to_be_sent = json.dumps(html_to_nodes(html_content))
        response = requests.get('https://api.telegra.ph/createPage?access_token={}&title=title&content={}&return_content=false'.format(access_token, content_to_be_sent))

        result = json.loads(response.text)['result']

        return result['url']
