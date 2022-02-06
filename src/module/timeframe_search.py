from typing import List
from finam import Timeframe

def get_all_timeframe()->List[str]:
    return [e.name for e in Timeframe]