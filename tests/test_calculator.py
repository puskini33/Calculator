import unittest
from runner import *


class TestCalculator(unittest.TestCase):

    def test_calculator(self):
        test_scanner = SetupScanner(TOKENS, code)

        test_parser = SetupParser(test_scanner.scanned_tree)
        test_parsed_string = test_parser.parse()
        print(test_parsed_string)

        test_world_state = WorldState()

        test_analyzer = SetupAnalyzer(test_parsed_string)
        test_analyzed_string = test_analyzer.analyze(test_world_state)

        test_interpreter = SetupInterpreter(test_analyzed_string)
        test_interpreted_tree = test_interpreter.interpret(test_world_state)


code = ["1 + 2 ="]

TOKENS = [
            ((r"^[0-9]+"),                 "INTEGER"),
            ((r"^\+"),                     "PLUS"),
            ((r"\s"),                      "SPACE"),
            ((r"\="),                      "EQUAL"),
            ((r"[a-z]"),                   "VARIABLE")]


if __name__ == "__main__":
    TestCalculator()
