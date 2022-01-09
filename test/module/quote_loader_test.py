import datetime 
import unittest
from src.module.quote_loader import load_quote
from pandas_data_reader_service_core.modules.finam.stock_info import FinamStockInfo, Market
from pandas_data_reader_service_core.modules.finam.download_service import TimeFrame
import pandas as pd


class quote_search_TestCase(unittest.TestCase):
    def test_load_quote(self):
        stock_info = FinamStockInfo.by_code("EURUSD", Market.CURRENCIES_WORLD)
        args = {
            "stock_info": stock_info,
            "start_date": datetime.date(2020, 1, 1),
            "end_date": datetime.date(2020, 1, 1),
            "timeframe": TimeFrame.HOURLY
        }
        asserted_df = load_quote(**args)

        excepted_df = pd.DataFrame({
            "DateTime": [
                "2020-01-01T00:00:00",
                "2020-01-01T02:00:00",
                "2020-01-01T20:00:00",
                "2020-01-01T21:00:00",
                "2020-01-01T22:00:00",
                "2020-01-01T23:00:00",
                "2020-01-02T00:00:00"
            ],
            "Open": [1.12172,1.12123,1.12154,1.12080,1.12130,1.12130,1.12123],
            "High": [1.12174,1.12123,1.12154,1.12214,1.12159,1.12180,1.12126],
            "Low": [1.12079,1.12117,1.12154,1.12080,1.12120,1.12100,1.12100],
            "Close": [1.12110,1.12117,1.12154,1.12124,1.12127,1.12134,1.12126],
            "Volume": [12821,2,1,63,70,56,3]})

        self.assertTrue(asserted_df.equals(excepted_df))