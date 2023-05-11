import requests
import json


def uploadImage(img_path):
    """Upload an image to https://telegra.ph/

    Uploads an image to telegraph's database and returns a link to it.
    Can be used for the page creation

    """
    with open(img_path, 'rb') as imageF:
        image_extension = img_path.split('.').pop()

        response = requests.post(
            'https://telegra.ph/upload',
            files={'file': ('file', imageF, 'image/{}'.format(image_extension))}
        )

        if not str(response.status_code).startswith('2'):
            return False
        
        image_uploaded = json.loads(response.text)

        if not ('error' in image_uploaded):
            return image_uploaded[0]['src'], False
        else:
            return False, image_uploaded['error']
