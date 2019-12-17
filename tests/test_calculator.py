import unittest
from StringScanner import Scanner
from StringParser import Parser


class TestCalculator(unittest.TestCase):

    def test_scanner(self):
        local_scanner = Scanner(TOKENS, code)
        local_parser = Parser(local_scanner)
        parse_tree = local_parser.main()
        self.assertNotEqual(parse_tree, None)
        print(parse_tree)


code = ["x = 10", "y = 11", "j = x + y", "1 + 2 ="]

TOKENS = [
            ((r"^[0-9]+"),                 "INTEGER"),
            ((r"^\+"),                     "PLUS"),
            ((r"\s"),                      "SPACE"),
            ((r"\="),                      "EQUAL"),
            ((r"[a-z]"),                   "VARIABLE")]


if __name__ == "__main__":
    TestCalculator()
