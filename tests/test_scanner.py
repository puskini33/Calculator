from string_scanner.scanner import Scanner
from string_scanner.scanner_string_segment import ScannedStringSegment
from regex_tokens.enum_tokens import TokenName
from regex_tokens.regex_rules import RegexRules
import unittest


class TestScanner(unittest.TestCase):

    def test_scan(self):
        regex_rules = RegexRules()
        local_token_name = TokenName.integer.value
        local_scanner = Scanner(regex_rules.list_regex_rules, '1')
        self.assertEqual(local_scanner.list_tokens, [ScannedStringSegment(local_token_name, 0, 1, 1)])
        # self.assertRaises(AssertionError, lambda: Scanner(regex_rules.list_regex_rules, code))  # TODO: Ask what is the role of testing for errors. Is it to catch the errors in advance to deal with them afterwards in the code?

    def test_match(self):
        regex_rules = RegexRules()
        code = ["1 + 2 ="]
        test_local_scanner = Scanner(regex_rules.list_regex_rules, code)
        self.assertEqual(test_local_scanner.match('INTEGER'), ['INTEGER', '1'])
        self.assertEqual(test_local_scanner.peek(), 'PLUS')
        # self.assertEqual(test_local_scanner.skip('PLUS'), True)
        # self.assertEqual(test_local_scanner.push(('PLUS', '+')), None)


if __name__ == "__main__":
    TestScanner()
