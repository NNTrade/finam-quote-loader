from finam import LookupComparator, Exporter, Market,FinamObjectNotFoundError
import pandas as pd
from finam import Exporter,LookupComparator
from typing import Tuple

def get_stock(**kwargs):
    if 'code' in kwargs.keys():        
        kwargs["code_comparator"] = LookupComparator.CONTAINS
    try:
        ret_df =  Exporter().lookup(**kwargs).reset_index()
        ret_df["market"] = ret_df["market"].apply(lambda el: Market(el).name)
        return ret_df
    except FinamObjectNotFoundError:
        return pd.DataFrame()
    

def by_code(code:str, market:Market)-> Tuple[int,Market]:
    stock_list = Exporter().lookup(code=code, market=market,code_comparator=LookupComparator.EQUALS )
                
    if len(stock_list) == 0:
        raise FinamObjectNotFoundError()
    if len(stock_list) > 1:
        raise Exception("More than 1 stock have been found")

    return stock_list.index[0], Market(stock_list["market"][stock_list.index[0]])    
    
