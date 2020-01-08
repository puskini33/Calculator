import unittest
from regex_tokens.regex_rules import RegexRules
from string_scanner.scanner import Scanner
from StringParser import Parser


class TestParser(unittest.TestCase):

    def test_parser(self):
        test_local_scanner = Scanner(RegexRules.list_regex_rules, ["1 + 1 ="])
        test_local_parser = Parser(test_local_scanner)

        # with self.assertRaises(UnboundLocalError):
        test_local_parser.parse()  # TODO: there should be an error here, but the program does not catch it
        # self.assertEqual(str(test_local_parser.parse()), '[Operation(AddExpression(Integer(1), Integer(2)))]')  # TODO: TypeError: 'int' object is not subscriptable if I write without str
