from finam import LookupComparator, Exporter, Market,FinamObjectNotFoundError
import pandas as pd

def get_stock(**kwargs):
    if 'code' in kwargs.keys():
        
        kwargs["code_comparator"] = LookupComparator.CONTAINS
    try:
        ret_df =  Exporter().lookup(**kwargs).reset_index()
        ret_df["market"] = ret_df["market"].apply(lambda el: Market(el).name)
        return ret_df
    except FinamObjectNotFoundError:
        return pd.DataFrame()
    
