from pandas_data_reader_service_core.modules.finam.stock_info import Market

def get_all_markets():
    return [e.name for e in Market]