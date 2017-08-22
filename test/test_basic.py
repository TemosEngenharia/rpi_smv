import unittest
import os

from app import radar


class BasicTestCase(unittest.TestCase):
    def test_index(self):
        tester = radar.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_database_file(self):
        tester = os.path.exists('/etc/radar/config.py')
        self.assertTrue(tester)

if __name__ == '__main__':
    unittest.main()
