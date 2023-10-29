from unittest import TestCase
from util.time_util import ts10_to_date_str, ts13_to_date_str

class TestMySQLUtil(TestCase):
    def setUp(self) -> None:
        pass

    def test_ts10_to_date_str(self):
        ts = 1652840528
        expected = '2022-05-18 12:22:08'
        result = ts10_to_date_str(ts)
        self.assertEqual(expected, result)

        result = ts10_to_date_str(1652840528, format_string="%Y%m%d%H%M%S")
        self.assertEqual("20220518122208", result)

    def test_ts13_to_date_str(self):
        ts = 1652840528123
        expected = '2022-05-18 12:22:08'
        result = ts13_to_date_str(ts)
        self.assertEqual(expected, result)

        result = ts13_to_date_str(1652840528123, format_string="%Y%m%d%H%M%S")
        self.assertEqual("20220518122208", result)