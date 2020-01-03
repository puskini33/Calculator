from StringInterpreter import Interpreter
from grammar_productions import *
import unittest


class TestInterpreter(unittest.TestCase):

    def test_interpreter(self):
        test_local_interpreter = Interpreter(AddExpression(Integer(1), Integer(2)))  # TODO: TypeError: 'int' object is not subscriptable
