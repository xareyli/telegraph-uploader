import unittest
from PIL import Image

import sys
import os
sys.path.append(os.path.abspath('../'))

from image import scaleImage

class ScaleImageTest(unittest.TestCase):
    def test_correctness(self):
        img_to_scale = 'assets/image.jpg'

        itsF = Image.open(img_to_scale)

        scale_ratio = 0.5
        expected_width = int(itsF.size[0] * scale_ratio)
        expected_height = int(itsF.size[1] * scale_ratio)

        scaled_path = scaleImage(img_to_scale, 'assets/', .5)

        with Image.open(scaled_path) as result_imgF:
            result_width, result_height = result_imgF.size

        self.assertEqual(result_width, expected_width, 'Width is wrong')
        self.assertEqual(result_height, expected_height, 'Height is wrong')

        os.remove(scaled_path)

    def test_invalid_path(self):
        invalid_img_path = 'invalid_path/test _image.jpg'
        save_path = 'assets/'
        scale_ratio = 0.5

        with self.assertRaises(FileNotFoundError):
            scaleImage(invalid_img_path, save_path, scale_ratio)

        img_path = 'assets/image.jpg'
        invalid_save_path = 'nonexisting/'
        scale_ratio = 0.5

        with self.assertRaises(ValueError):
            scaleImage(img_path, invalid_save_path, scale_ratio)

    def test_invalid_args(self):
        with self.assertRaises(ValueError):
            scaleImage(False, 'save_path', .5)
            scaleImage('assets/image.jpg', False, .5)
            scaleImage('assets/image.jpg', 'assets/', False)


if __name__ == "__main__":
    unittest.main()
