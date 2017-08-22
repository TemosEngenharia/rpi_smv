import unittest
import app
import test.all_tests


testSuite = test.all_tests.create_test_suite()
test_runner = unittest.TextTestRunner().run(testSuite)
