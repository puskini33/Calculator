from string_scanner.scanner import Scanner
from string_scanner.scanner_string_segment import ScannedStringSegment
from regex_tokens.enum_tokens import TokenName
from regex_tokens.regex_rules import RegexRules
import unittest


class TestScanner(unittest.TestCase):

    def test_scaner(self):
        local_token_name = TokenName.integer.value
        local_scanner = Scanner(RegexRules.list_regex_rules, ['1'])
        # self.assertEqual(local_scanner.list_tokens, [ScannedStringSegment(local_token_name, 0, 1, 1)])  # TODO: Figure it out why there is a difference
        # self.assertRaises(AssertionError, lambda: Scanner(regex_rules.list_regex_rules, code))  # TODO: Ask what is the role of testing for errors. Is it to catch the errors in advance to deal with them afterwards in the code?

        test_local_scanner_1 = Scanner(RegexRules.list_regex_rules, ["1 + 2 ="])
        self.assertEqual(test_local_scanner_1.match('INTEGER'), ['INTEGER', '1'])
        self.assertEqual(test_local_scanner_1.peek(), 'PLUS')
        self.assertEqual(test_local_scanner_1.skip('PLUS'), True)
        self.assertEqual(test_local_scanner_1.push(('PLUS', '+')), None)
        self.assertEqual(test_local_scanner_1.done(), False)
        test_local_scanner_2 = Scanner(RegexRules.list_regex_rules, '1')
        self.assertEqual(test_local_scanner_2.match('INTEGER'), ['INTEGER', '1'])
        self.assertEqual(test_local_scanner_2.done(), True)


if __name__ == "__main__":
    TestScanner()
