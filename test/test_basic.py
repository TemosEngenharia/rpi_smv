import os
import unittest

from app import rpi_smv
import config


class BasicTestCase(unittest.TestCase):
    def test_index(self):
        tester = rpi_smv.app.test_client(self)
        response = tester.get('/', content_type = 'html/text')
        self.assertEqual(response.status_code, 404)

    def test_database_dir(self):
        tester = os.path.exists(config.BASE_DB_DIR)
        self.assertTrue(tester)

    def test_log_dir(selfself):
        tester = os.path.exists(config.BASE_LOG_DIR)
        self.assertTrue(tester)

if __name__ == '__main__':
    unittest.main()
