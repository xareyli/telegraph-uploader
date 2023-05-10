import requests
import json
from utils import html_to_nodes


def createAccount(self, short_name, author_name):
    """Create a new user account on https://telegra.ph/

    Creates an account with given credentials and returns servers response, False if couldn't create an account

    """
    account = requests.post('https://api.telegra.ph/createAccount?short_name={}&author_name={}'.format(short_name, author_name))

    resp_decoded = json.loads(account.content.decode())

    if not resp_decoded['ok'] or not str(account.status_code).startswith('2'):
        return account.json()['result']
    else:
        return False


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


def createPage(access_token, image_sources):
    """Create a page on https://telegra.ph/

    Accepts a list of image sources and creates a page containing those images.
    Returns the url of the page in case of success, False otherwise

    """
    # create html skeleton of the page
    html_content = ''

    for src in image_sources:
        html_content = html_content + "<img src='{}' />".format(src)

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
