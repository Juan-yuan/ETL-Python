from unittest import TestCase
from util.str_util import check_null, check_str_null_and_transform_to_sql_null

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

    def check_check_str_null_and_transform_to_sql_null(self):
        name = ""
        result = check_str_null_and_transform_to_sql_null(name)
        self.assertEqual("NULL", name)

        name = "None"
        result = check_str_null_and_transform_to_sql_null(name)
        self.assertEqual("NULL", name)

        name = "null"
        result = check_str_null_and_transform_to_sql_null(name)
        self.assertEqual("NULL", name)

        name = "undefined"
        result = check_str_null_and_transform_to_sql_null(name)
        self.assertEqual("NULL", name)

        name = 'John'
        name = check_str_null_and_transform_to_sql_null(name)
        self.assertEqual('John', name)