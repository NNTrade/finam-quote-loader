from typing import Dict

class ArgsException(Exception):
    def __init__(self, dic:Dict[str,str] = {}):
        self.dic:Dict[str,str] = dic
        pass

    def to_output(self):
        return str(self.dic)