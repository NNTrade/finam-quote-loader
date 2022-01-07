from finam import Market,Timeframe, Exporter,LookupComparator
import datetime
from .excepiton import ArgsException
from typing import Dict
import pandas as pd

def load_quote(**kwargs):
    df = Exporter().download(id_=kwargs["id_"], market=kwargs["market"],start_date=kwargs["start_date"], end_date=kwargs["end_date"], timeframe=kwargs["timeframe"])
    
    df = df.rename(columns={"<OPEN>":"O", "<HIGH>":"H", "<LOW>":"L", "<CLOSE>":"C", "<VOL>":"V"})
    
    df["DT"] = df.apply(lambda row: f'{row["<DATE>"]}-{row["<TIME>"][:2]}{row["<TIME>"][3:5]}',axis=1)
    
    df = df.drop(['<DATE>', '<TIME>'], axis=1)\
                .reindex(["DT","O","H","L","C","V"], axis=1)
    return df

def parse_args(args:Dict)->Dict:
    stock =  args.get('code')
    market =  args.get('market')
    date_from = args.get('from')
    date_till = args.get('till')
    timeframe = args.get('tf')
    
       
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
        tf_enum = Timeframe[timeframe]
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
    
    df = Exporter().lookup(market = market_enum, code=stock, code_comparator=LookupComparator.EQUALS)
    
    if len(df) == 0:
        ex.dic["code"] = "Cannot find record for code"    
    if len(df) > 1:
        ex.dic["code"] = "Found more than 1 variant"    
    
    if len(ex.dic) > 0:
        raise ex
    
    id = df.iloc[0].name
    
    return {"id_":id, "market":market_enum, "start_date":dt_from, "end_date":dt_till, "timeframe":tf_enum}
    
    
    
