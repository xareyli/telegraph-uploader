import requests
import json
from libs.html_parser import html_to_nodes


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
