import unittest
from StringScanner import Scanner


class TestScanner(unittest.TestCase):

    def test_match(self):
        code = ["1 + 2 ="]

        TOKENS = [
                    ((r"^[0-9]+"),                 "INTEGER"),
                    ((r"^\+"),                     "PLUS"),
                    ((r"\s"),                      "SPACE"),
                    ((r"\="),                      "EQUAL"),
                    ((r"[a-z]"),                   "VARIABLE")]

        test_local_scanner = Scanner(TOKENS, code)

        self.assertEqual(test_local_scanner.match('INTEGER'), ['INTEGER', '1'])
        self.assertEqual(test_local_scanner.peek(), 'PLUS')
        self.assertEqual(test_local_scanner.skip('PLUS'), True)
        self.assertEqual(test_local_scanner.push(('PLUS', '+')), None)


if __name__ == "__main__":
    TestScanner()
