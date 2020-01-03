import unittest
from StringScanner import Scanner
from StringParser import Parser


class TestParser(unittest.TestCase):

    def test_parser(self):
        code = ["1 + 2 ="]

        TOKENS = [
                    ((r"^[0-9]+"),                 "INTEGER"),
                    ((r"^\+"),                     "PLUS"),
                    ((r"\s"),                      "SPACE"),
                    ((r"\="),                      "EQUAL"),
                    ((r"[a-z]"),                   "VARIABLE")]

        test_local_scanner = Scanner(TOKENS, code)
        test_local_parser = Parser(test_local_scanner)

        self.assertEqual(str(test_local_parser.root()), 'AddExpression(Integer(1), Integer(2))')  # TODO: TypeError: 'int' object is not subscriptable if I write without str
