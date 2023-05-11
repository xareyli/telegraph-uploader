import unittest

import sys
import os
sys.path.append(os.path.abspath('../'))

from create_account import createAccount

class CreateAccountTest(unittest.TestCase):
    def test_correctness(self):
        account = createAccount('tst_sht', 'author_name')

        self.assertNotEqual(account, False, 'Can\'t create an account')

        self.assertEqual(account['short_name'], 'tst_sht', 'Short name is wrong')
        self.assertEqual(account['author_name'], 'author_name', 'Author name is wrong')

        self.assertTrue(account['access_token'], 'Access token is not present')
        self.assertTrue(account['auth_url'], 'Auth url is not present')

    def test_invalid_args(self):
         with self.assertRaises(TypeError):
            createAccount(1, 'author_name')
            createAccount('short_name', 1)


if __name__ == "__main__":
     unittest.main()
