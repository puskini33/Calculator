from StringScanner import Scanner
from StringParser import Parser
from StringAnalyzer import Analyzer
from StringInterpreter import Interpreter


class SetupScanner(object):
    """docstring for LocalScanner"""
    def __init__(self, regex_rules, text_to_match):
        self.regex_rules = regex_rules
        self.text_to_match = text_to_match
        self.scanned_tree = Scanner(regex_rules, text_to_match)


class SetupParser(object):

    def __init__(self, scanned_tree):
        self.scanned_tree = scanned_tree
        self.local_parser = Parser(self.scanned_tree)

    def parse(self):
        result = []  # parse_tree
        while not self.scanned_tree.done():
            result.append(self.local_parser.root())

        return result


class SetupAnalyzer(object):

    def __init__(self, parsed_tree):
        self.parsed_tree = parsed_tree
        self.local_analyzer = Analyzer(self.parsed_tree)

    def analyze(self, local_world_state):
        return self.local_analyzer.analyze(local_world_state)


class SetupInterpreter(object):

    def __init__(self, analyzed_tree):
        self.analyzed_tree = analyzed_tree
        self.local_interpreter = Interpreter(self.analyzed_tree)

    def interpret(self, local_world_state):
        return self.local_interpreter.interpret(local_world_state)


class WorldState(object):

    def __init__(self):
        self.variables = {}


code = ["1 * 2"]

TOKENS = [
        ((r"^[0-9]+"),                 "INTEGER"),
        ((r"^\+"),                     "PLUS"),
        ((r"-"),                       "MINUS"),
        ((r"\/"),                       "DIVISION SIGN"),
        ((r"\*"),                      "TIMES SIGN"),
        ((r"%"),                       "MODULO SIGN"),
        ((r"\s"),                      "SPACE"),
        ((r"\="),                      "EQUAL"),
        ((r"[a-z]"),                   "VARIABLE")]

setup_scanner = SetupScanner(TOKENS, code)

setup_parser = SetupParser(setup_scanner.scanned_tree)
parsed_string = setup_parser.parse()
print(parsed_string)

world_state = WorldState()

setup_analyzer = SetupAnalyzer(parsed_string)
analyzed_string = setup_analyzer.analyze(world_state)

setup_interpreter = SetupInterpreter(analyzed_string)
interpreted_tree = setup_interpreter.interpret(world_state)
