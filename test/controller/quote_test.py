import unittest
from pandas_data_reader_service_core.modules.TimeFrame import TimeFrame

from pandas_data_reader_service_core.modules.finam.stock_info import FinamStockInfo
from src.controllers.quote import verify_args
from datetime import date

class quote_loader_args_parse_TestCase(unittest.TestCase):

    def test_get_args(self):
        args={"code": "EURUSD", "market":"CURRENCIES_WORLD", "from":"2020-01-01","till":"2021-02-02", "tf":"HOURLY"}
        
        asserted_args = verify_args(**args)
        expected_info = FinamStockInfo(83)
        
        self.assertEqual(expected_info, asserted_args["stock_info"])
        self.assertEqual(date(2020,1,1), asserted_args["start_date"])
        self.assertEqual(date(2021,2,2), asserted_args["end_date"])
        self.assertEqual(TimeFrame.HOURLY, asserted_args["timeframe"])
        