import unittest
from typing import List
from src.module.quote_loader import parse_args
from finam import Market,Timeframe
from datetime import date

class quote_loader_args_parse_TestCase(unittest.TestCase):

    def test_get_args(self):
        args={"code": "EURUSD", "market":"CURRENCIES_WORLD", "from":"2020-01-01","till":"2021-02-02", "tf":"HOURLY"}
        
        asserted_args = parse_args(args)
        
        self.assertEqual(83, asserted_args["id_"])
        self.assertEqual(Market.CURRENCIES_WORLD, asserted_args["market"])
        self.assertEqual(date(2020,1,1), asserted_args["start_date"])
        self.assertEqual(date(2021,2,2), asserted_args["end_date"])
        self.assertEqual(Timeframe.HOURLY, asserted_args["timeframe"])
        