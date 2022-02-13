from datetime import datetime
import pandas as pd
from finam import Exporter, Market,Timeframe, FinamParsingError
import logging

def load_quote(stock_idx:int, market: Market, start_date:datetime, end_date:datetime, timeframe:Timeframe)->pd.DataFrame:
    logger = logging.getLogger("load_quote")
    logger.info(f'Load quote for: stock_idx = {stock_idx}, market = {market}, date_from = {start_date}, date_till = {end_date}, timframe = {timeframe}')
    
    try:
        ret:pd.DataFrame = Exporter().download(stock_idx,market,start_date,end_date,timeframe )
    except FinamParsingError as ex:
        logger.warning(f"Get error while parsing: {ex}")    
        raise ex
    
    if len(ret.index) == 0:  
        return ret
    ret.rename(columns={"<CLOSE>": "Close", "<OPEN>": "Open", "<HIGH>": "High", "<LOW>": "Low", "<VOL>": "Volume"},
                    inplace=True)
    ret["DT"] = ret.apply(lambda row:
                    pd.Timestamp(
                        year=int(str(row["<DATE>"])[:4]),
                        month=int(str(row["<DATE>"])[4:6]),
                        day=int(str(row["<DATE>"])[6:8]),
                        hour=int(str(row["<TIME>"]).split(":")[0]),
                        minute=int(str(row["<TIME>"]).split(":")[1])), axis=1)
    ret = ret.drop(["<DATE>", "<TIME>"], axis=1).reset_index().sort_values(by=["DT"])
    ret = ret[~ret["DT"].duplicated(keep='first')].reset_index()
    ret = ret.round(9)
    ret["DT"] = ret["DT"].map(lambda el: el.isoformat())
    return ret
  
