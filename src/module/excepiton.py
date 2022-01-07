from typing import Dict

class ArgsException(Exception):
    def __init__(self, dic = {}):
        self.dic = dic
        pass

    def to_output(self):
        return str(self.dic)