import requests
import json


def uploadImage(img_path):
    """Upload an image to https://telegra.ph/

    Uploads an image to telegraph's database and returns a link to it.
    Can be used for the page creation

    """
    try:
        imageF = open(img_path, 'rb')
    except OSError as e:
        raise OSError('Error opening file: {}'.format(str(e)))

    try:
        image_extension = img_path.split('.').pop()

        response = requests.post(
            'https://telegra.ph/upload',
            files={'file': ('file', imageF, 'image/{}'.format(image_extension))}
        )

        response.raise_for_status()

        image_uploaded = json.loads(response.text)
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException('Error uploading image: {}'.format(str(e)))
    except ValueError as e:
        raise ValueError('Error decoding server response: {}'.format(str(e)), e.doc, e.pos)
    except Exception as e:
        raise Exception('An unexpected error occurred: {}'.format(str(e)))

    if not ('error' in image_uploaded):
        return image_uploaded[0]['src']
    else:
        raise ValueError(image_uploaded['error'])
