import unittest
from regex_tokens.regex_rules import RegexRules
from string_scanner.scanner import Scanner
from string_parser import Parser


class TestParser(unittest.TestCase):

    def test_parser(self):
        test_local_scanner = Scanner(RegexRules.list_regex_rules, ["1 + 1 ="])
        test_local_parser = Parser(test_local_scanner)

        test_local_parser.parse()
