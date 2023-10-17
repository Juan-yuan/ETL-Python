import logging
from unittest import TestCase
from util.logging_util import init_logger


class TestLoggingUtil(TestCase):
    def setUp(self) -> None:
        pass

    def test_logger(self):
        logger = init_logger()
        result = isinstance(logger, logging.RootLogger)
        self.assertEqual(True, result)
