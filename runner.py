from string_scanner.scanner import Scanner
from StringParser import Parser
from StringAnalyzer import Analyzer
from StringInterpreter import Interpreter
from regex_tokens.regex_rules import RegexRules
from world_state import WorldState

code = ['13 * 7 =']

setup_scanner = Scanner(RegexRules.list_regex_rules, code)

setup_parser = Parser(setup_scanner)
parsed_string = setup_parser.parse()
print(parsed_string)

world_state = WorldState()

setup_analyzer = Analyzer(parsed_string)
analyzed_string = setup_analyzer.analyze(world_state)

setup_interpreter = Interpreter(analyzed_string)
interpreted_tree = setup_interpreter.interpret(world_state)
