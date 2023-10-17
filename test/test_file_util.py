import os
from unittest import TestCase
from util.file_util import get_dir_files_list


class TestFileUtil(TestCase):
    def setUp(self) -> None:
        # os.path.dirname(os.getcwd()) get current project root path
        self.project_root_path = os.path.dirname(os.getcwd())  # /Users/kityua/PycharmProjects-gaoji/ETL-Python

    def test_get_dir_files_list(self):
        test_path = f"{self.project_root_path}/test/test_dir"

        result = get_dir_files_list(test_path)  # recursion=False by default
        names = []
        for i in result:
            names.append(os.path.basename(i))
        # To prevent test failures caused by the order of results, it is necessary to sort 'names' in ascending order.
        names.sort()
        self.assertEqual(["1.txt", "2.txt"], names)

        # Testing recursion
        result = get_dir_files_list(test_path, recursion=True)
        names = []
        for i in result:
            names.append(os.path.basename(i))
        # To prevent test failures due to the order of results, it's necessary to sort the 'names' in ascending order.
        names.sort()
        self.assertEqual(['1.txt', '2.txt', '3.txt', '4.txt', '5.txt'], names)
