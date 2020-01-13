from string_scanner.scanner import Scanner
from string_parser import Parser
from string_analyzer import Analyzer
from string_interpreter import Interpreter
from regex_tokens.regex_rules import RegexRules
from world_state import WorldState

code = []


def ask_user():
    user_input = input('Please introduce the operation you would like to calculate: ')
    code.append(user_input)


def ask_user_again():
    second_user_input = input(' Would you like to introduce a new operation? yes/no:  ')
    if second_user_input == 'yes':
        ask_user()
        third_user_input = input(' Would you like to introduce a new operation? yes/no:  ')
        if third_user_input == 'yes':
            ask_user()


ask_user()
ask_user_again()

setup_scanner = Scanner(RegexRules.list_regex_rules, code)

setup_parser = Parser(setup_scanner)
parsed_string = setup_parser.parse()

world_state = WorldState()

setup_analyzer = Analyzer(parsed_string)
analyzed_string = setup_analyzer.analyze(world_state)

setup_interpreter = Interpreter(analyzed_string)
interpreted_tree = setup_interpreter.interpret(world_state)
