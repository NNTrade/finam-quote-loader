import unittest
from src.module.excepiton import ArgsException

class ArgsError_TestCase(unittest.TestCase):

    def test_parse_errors(self):
        argErr = ArgsException({'field1': 'error1', 'field2': 'error2'})
        self.assertEqual("{'field1': 'error1', 'field2': 'error2'}", argErr.to_output())