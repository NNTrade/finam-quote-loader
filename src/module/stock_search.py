from finam import Market, LookupComparator, Exporter, FinamObjectNotFoundError
import pandas as pd

def get_stock(**kwargs):
    if 'code' in kwargs.keys():
        kwargs["code_comparator"] = LookupComparator.CONTAINS
    try:
        return Exporter().lookup(**kwargs).reset_index()
    except FinamObjectNotFoundError:
        return pd.DataFrame()
    
def parse_args(args):
    market = request.args.get('market')
    code = request.args.get('code')
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
