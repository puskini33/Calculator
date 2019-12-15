import unittest
from scanner import Scanner
from parser import Parser


class TestCalculator(unittest.TestCase):

    def test_scanner(self):
        local_scanner = Scanner(TOKENS, code)
        local_parser = Parser(local_scanner)
        local_parser.main()



code = ["1 + 2 ="]

TOKENS = [
            ((r"^[0-9]+"),                 "INTEGER"),
            ((r"^\+"),                     "PLUS"),
            ((r"\s"),                      "SPACE"),
            ((r"\="),                      "EQUAL")]
