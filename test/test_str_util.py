from unittest import TestCase
from util.str_util import check_null

class TestStrUtil(TestCase):
    def setUp(self) -> None:
        pass

    def test_check_null(self):
        s = 'None'
        result = check_null(s)
        self.assertEqual(True, result)

        s = 'none'
        result = check_null(s)
        self.assertEqual(True, result)

        s = ''
        result = check_null(s)
        self.assertEqual(True, result)

        s = 'undefined'
        result = check_null(s)
        self.assertEqual(True, result)

        s = 'Not-null'
        result = check_null(s)
        self.assertEqual(False, result)