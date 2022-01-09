from finam.exception import FinamObjectNotFoundError
from pandas_data_reader_service_core.modules.exceptions import StockNotFoundException
from pandas_data_reader_service_core.modules.finam.download_service import TimeFrame
import datetime
from ..module.excepiton import ArgsException
from pandas_data_reader_service_core.modules.finam.stock_info import Market,FinamStockInfo
from flask_restx import reqparse

parser = reqparse.RequestParser()
parser.add_argument('market', type=str, help='market name', location='args')
parser.add_argument('code', type=str, help='stock code', location='args')
parser.add_argument('from', type=str, help='date from (format: YYYY-MM-DD)', location='args')
parser.add_argument('till', type=str, help='date till (format: YYYY-MM-DD)', location='args')
parser.add_argument('tf', type=str, help='timeframe', location='args')

def verify_args(**args):
    stock =     args['code']
    market =    args['market']
    date_from = args['from']
    date_till = args['till']
    timeframe = args['tf']
       
    if  stock is None or \
        date_from is None or \
        date_till is None or \
        timeframe is None or \
        market is None:
        ex = ArgsException()
        if stock is None:
            ex.dic["code"] = "Code must be filled"
        if market is None:
            ex.dic["market"] = "Market must be filled"
        if date_from is None:
            ex.dic["from"] = "From must be filled"
        if date_till is None:
            ex.dic["till"] = "Till must be filled"
        if timeframe is None:
            ex.dic["tf"] = "Tf (Timeframe) must be filled"
        raise ex
        
    ex = ArgsException()
    try:
        market_enum = Market[market]
    except Exception:
        ex.dic["market"] = "Cannot parse market value"
        
    try:
        tf_enum = TimeFrame[timeframe]
    except Exception:
        ex.dic["tf"] = "Cannot parse tf (Timeframe) value"
    
    format = '%Y-%m-%d'
    
    try:
        dt = datetime.datetime.strptime(date_from, format)
        dt_from = dt.date()
    except Exception:
        ex.dic["from"] = "Cannot parse from date value"    
    
    try:
        dt = datetime.datetime.strptime(date_till, format)
        dt_till = dt.date()
    except Exception:
        ex.dic["till"] = "Cannot parse till date value"    
    
    try:
        finamStockInfo = FinamStockInfo.by_code(stock, market_enum)
    except StockNotFoundException:
        ex.dic["code"] = "Cannot find record for code"    
    except Exception:
        ex.dic["code"] = "Found more than 1 variant"    
    
    if len(ex.dic) > 0:
        raise ex
    
    return {"stock_info":finamStockInfo, "start_date":dt_from, "end_date":dt_till, "timeframe":tf_enum}
    