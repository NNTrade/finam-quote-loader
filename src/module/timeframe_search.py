from typing import List
from pandas_data_reader_service_core.service import TimeFrame

def get_all_timeframe()->List[str]:
    return [e.name for e in TimeFrame]