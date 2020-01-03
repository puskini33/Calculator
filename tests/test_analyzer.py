from StringAnalyzer import Analyzer
from grammar_productions import *
import unittest


class TestAnalyzer(unittest.TestCase):

    def test_analyzer(self):
        test_local_analyzer = Analyzer(AddExpression(Integer(1), Integer(2)))  # TODO: TypeError: 'int' object is not subscriptable
