import unittest
from typing import List
from src.module.stock_search import get_stock
from finam import Market

class stock_search_TestCase(unittest.TestCase):

    def test_get_market(self):
        market = Market.USA
        code = "CINF"
        args = {}
        if market is not None:
            args["market"] = market
        if code is not None:
            args["code"] = code
        ret = get_stock(**args)

        self.assertEqual(1, len(ret))
    
    def test_get_several_markets(self):
        market = Market.USA
        code = "CI"
        args = {}
        if market is not None:
            args["market"] = market
        if code is not None:
            args["code"] = code
        ret = get_stock(**args)

        self.assertTrue(len(ret)>1)