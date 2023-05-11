import unittest

import sys
import os
sys.path.append(os.path.abspath('../'))

from upload_image import uploadImage

class CreateAccountTest(unittest.TestCase):
    def test_correctness(self):
        normal_img = 'assets/normal.jpg'

        result = uploadImage(normal_img)

        self.assertNotEqual(result, False, 'Couldn\'t upload the image')

        self.assertTrue(result.split('/')[1] == 'file', 'invalid source link')

    def test_nonexisting_image(self):
        nonexisting_img = 'assets/nonexisting.jpg'

        with self.assertRaises(OSError):
            uploadImage(nonexisting_img)

    def test_invalid_image(self):
        invalid_img = 'assets/invalid.jpg'

        with self.assertRaises(ValueError):
            uploadImage(invalid_img)

    def test_no_image(self):
        text_file = 'assets/no_image.txt'

        with self.assertRaises(ValueError):
            uploadImage(text_file)


if __name__ == "__main__":
    unittest.main()
