import unittest
from finam import Market,Timeframe
from src.controllers.QuoteController import QuoteController
from datetime import date

class quote_loader_args_parse_TestCase(unittest.TestCase):

    def test_get_args(self):
        args={"code": "EURUSD", "market":"CURRENCIES_WORLD", "from":"2020-01-01","till":"2021-02-02", "tf":"HOURLY"}
        
        asserted_idx, asserted_market, asserted_dt_from, asserted_dt_till, asserted_tf = QuoteController.verify_args(**args)

        self.assertEqual(83, asserted_idx)
        self.assertEqual(Market.CURRENCIES_WORLD, asserted_market)
        self.assertEqual(date(2020,1,1), asserted_dt_from)
        self.assertEqual(date(2021,2,2), asserted_dt_till)
        self.assertEqual(Timeframe.HOURLY, asserted_tf)
        