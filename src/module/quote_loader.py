from pandas_data_reader_service_core.modules.finam.download_service import FinamStockDownloadService
import pandas as pd

def load_quote(**kwargs)->pd.DataFrame:
    df = FinamStockDownloadService().get_by_stock_info(stock_info=kwargs["stock_info"], date_from=kwargs["start_date"], date_to=kwargs["end_date"], time_frame=kwargs["timeframe"])
    
    df = df.reset_index().rename({"DT":"DateTime","O":"Open","H":"High","L":"Low","C":"Close","V":"Volume"},axis=1)
    df["DateTime"] = df["DateTime"].apply(lambda el: el.isoformat())
    return df


    
    
