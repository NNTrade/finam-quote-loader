import unittest
from typing import List
from src.module.market_search import get_all_markets

class market_search_TestCase(unittest.TestCase):

    def test_get_all_markets(self):
        ret = get_all_markets()

        self.assertIsInstance(ret, List)