from string_scanner.scanner import Scanner
from StringParser import Parser
from StringAnalyzer import Analyzer
from StringInterpreter import Interpreter
from regex_tokens.regex_rules import RegexRules

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

local_regex_rules = RegexRules()

setup_scanner = Scanner(local_regex_rules.list_regex_rules, code)

setup_parser = Parser(setup_scanner)
parsed_string = setup_parser.parse()
print(parsed_string)




world_state = WorldState()

setup_analyzer = SetupAnalyzer(parsed_string)
analyzed_string = setup_analyzer.analyze(world_state)

setup_interpreter = SetupInterpreter(analyzed_string)
interpreted_tree = setup_interpreter.interpret(world_state)
