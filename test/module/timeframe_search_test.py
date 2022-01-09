import unittest

from src.module.timeframe_search import get_all_timeframe

class timeframe_search_TestCase(unittest.TestCase):
    def test_get(self):
        print(get_all_timeframe())