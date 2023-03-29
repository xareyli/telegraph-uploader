import requests
import os
from utils import scaleImage, getImageExtension, html_to_nodes, getImageDimensions
import logging
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
                raise Exception('API: response code differs from 2xx')

            logging.info('API: account created successfuly')

            return account.json()['result']
        except Exception as e:
            logging.error('[ERROR]: ' + str(e))
            return False

    def upload(self, access_token, imgDir, callback):
        html_content = ""

        number_uploaded = 0

        for path,subdir,files in os.walk(imgDir):
            for name in files:
                is_resized = False
                fullpath = os.path.join(path,name)

                image_dimensions = getImageDimensions(fullpath)

                if (image_dimensions[1] > 5500) or (image_dimensions[0] > 3500):
                    fullpath = self.fitImageIntoDimensions(fullpath, image_dimensions, (5500, 3500))
                    is_resized = True

                number_uploaded += 1
                is_size_small_enough = os.stat(fullpath).st_size / (1024 * 1024) < 5

                if not is_size_small_enough:
                    fullpath = self.shrinkImageUntilSizeSmallEnough(fullpath, 5)
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
                        callback(True, number_uploaded, fullpath)
                    else:
                        logging.warning('[API]: skipped "{}" due to "{}"'.format(fullpath, image_uploaded['error']))
                        callback(False, number_uploaded, fullpath)

                # remove thumbnail
                if is_resized:
                    os.remove(fullpath)

        content_to_be_sent = json.dumps(html_to_nodes(html_content))

        page_object = {
            "access_token": access_token,
            "title": "Title",
            "content": content_to_be_sent
        }

        response = requests.post('https://api.telegra.ph/createPage', data=page_object)

        if str(response.status_code).startswith('2') and not ('error' in response.text):
            result = json.loads(response.text)

            return result['result']['url']
        else:
            return False

    def shrinkImageUntilSizeSmallEnough(self, image_path, size_needed):
        original_filepath = image_path
        is_size_small_enough = os.stat(image_path).st_size / (1024 * 1024) < size_needed
        scale_ratio = .75
        # if the image is more than size_needed Mb, resize it
        while not is_size_small_enough:
            image_path = scaleImage(image_path, scale_ratio)

            is_size_small_enough = os.stat(image_path).st_size / (1024 * 1024) < size_needed

            if not is_size_small_enough:
                os.remove(image_path)
                scale_ratio -= .05
                image_path = original_filepath

        return image_path

    def fitImageIntoDimensions(self, image_path, current_dimensions, dimensions_needed):
        to_fit_height_scale_ratio = (dimensions_needed[1] * 100 / current_dimensions[1]) / 100
        to_fit_width_scale_ratio = (dimensions_needed[0] * 100 / current_dimensions[0]) / 100

        scale_ratio = min(to_fit_height_scale_ratio, to_fit_width_scale_ratio)

        return scaleImage(image_path, scale_ratio)
