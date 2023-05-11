import unittest

import sys
import os
sys.path.append(os.path.abspath('../'))
sys.path.append(os.path.abspath('../../../'))

from create_page import createPage
from create_account import createAccount
from upload_image import uploadImage

class CreatePageTest(unittest.TestCase):
    def setUp(self):
        self.access_token = createAccount('tst_sht', 'author_name')['access_token']
        self.image_sources = []

        self.image_sources.append(uploadImage('assets/normal.jpg'))

    def test_correctness(self):
        page_url = createPage(self.access_token, self.image_sources)

        self.assertTrue(page_url.startswith('https'), 'Value different from page url returned')

    def test_invalid_token(self):
        with self.assertRaises(ValueError):
            createPage('invalid_token', self.image_sources)

    def test_invalid_sources(self):
        with self.assertRaises(ValueError):
            createPage(self.access_token, [])
            createPage(self.access_token, False)


if __name__ == "__main__":
     unittest.main()
