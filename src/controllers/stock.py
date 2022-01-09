from finam.const import Market
from flask_restx import reqparse
from ..module.excepiton import ArgsException 
parser = reqparse.RequestParser()
parser.add_argument('market', type=str, help='market name', location='args')
parser.add_argument('code', type=str, help='stock code', location='args')

def verify_args(**args):
    market = args['market']
    code = args['code']
    args = {}
    
    ex = ArgsException()
    if market is not None:
        try:
            args["market"] = Market[market]  
        except Exception:
            ex.dic["tf"] = "Cannot parse tf (Timeframe) value"
           
    if code is not None:
        args["code"] = code
        
    if len(args) == 0:
        ex.dic["-"] = "Request must have market or code as query parameter"
    
    if len(ex.dic) > 0:
        raise ex

    return args
