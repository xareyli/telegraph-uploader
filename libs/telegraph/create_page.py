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

    if not isinstance(image_sources, list) or len(image_sources) == 0:
        raise ValueError('No image sources provided')

    for src in image_sources:
        html_content = html_content + "<img src='{}' />".format(src)

    content_to_be_sent = json.dumps(html_to_nodes(html_content))

    page_object = {
        "access_token": access_token,
        "title": "Title",
        "content": content_to_be_sent
    }

    try:
        response = requests.post('https://api.telegra.ph/createPage', data=page_object)

        print(response)

        response.raise_for_status()

        result = json.loads(response.text)
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException('Error uploading image: {}'.format(str(e)))
    except ValueError as e:
        raise ValueError('Error decoding server response: {}'.format(str(e)), e.doc, e.pos)
    except Exception as e:
        raise Exception('An unexpected error occurred: {}'.format(str(e)))

    if not ('error' in result):
        return result['result']['url']
    else:
        raise ValueError(result['error'])
