import datetime
import unittest
from src.module.quote_loader import load_quote
from finam import Market, Timeframe
import pandas as pd
from src.module.stock_search import by_code


class quote_search_TestCase(unittest.TestCase):
    def test_load_quote(self):
        idx, market = by_code("EURUSD", Market.CURRENCIES_WORLD)
        asserted_df = load_quote(idx, market, datetime.date(
            2020, 1, 1), datetime.date(2020, 1, 1), Timeframe.HOURLY)

        excepted_df = pd.DataFrame({
            "DT": ["2020-01-01T00:00:00",
                   "2020-01-01T02:00:00",
                   "2020-01-01T20:00:00",
                   "2020-01-01T21:00:00",
                   "2020-01-01T22:00:00",
                   "2020-01-01T23:00:00",
                   "2020-01-02T00:00:00"],
            "Open": [1.12172, 1.12123, 1.12154, 1.12080, 1.12130, 1.12130, 1.12123],
            "High": [1.12174, 1.12123, 1.12154, 1.12214, 1.12159, 1.12180, 1.12126],
            "Low": [1.12079, 1.12117, 1.12154, 1.12080, 1.12120, 1.12100, 1.12100],
            "Close": [1.12110, 1.12117, 1.12154, 1.12124, 1.12127, 1.12134, 1.12126],
            "Volume": [12821, 2, 1, 63, 70, 56, 3]},
        )

        self.assertEqual(len(asserted_df.columns), len(excepted_df.columns))
        self.assertEqual(len(asserted_df.index), len(excepted_df.index))
        for col in asserted_df:
            for row in asserted_df.index:
                self.assertEqual(
                    asserted_df[col][row], excepted_df[col][row], f"Col {col}, Row {row}")