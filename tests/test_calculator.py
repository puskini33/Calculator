from world_state import WorldState
from StringParser import Parser
from StringAnalyzer import Analyzer
from StringInterpreter import Interpreter
from regex_tokens.regex_rules import RegexRules
from string_scanner.scanner import Scanner
import unittest



class TestCalculator(unittest.TestCase):

    def test_calculator(self):
        code = ["1 + 2 ="]
        regex_rules = RegexRules()
        test_scanner = Scanner(regex_rules.list_regex_rules, code)

        test_parser = Parser(test_scanner)
        test_parsed_string = test_parser.parse()
        print(test_parsed_string)

        test_world_state = WorldState()

        test_analyzer = SetupAnalyzer(test_parsed_string)
        test_analyzed_string = test_analyzer.analyze(test_world_state)

        test_interpreter = SetupInterpreter(test_analyzed_string)
        test_interpreted_tree = test_interpreter.interpret(test_world_state)




if __name__ == "__main__":
    TestCalculator()
