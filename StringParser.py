from StringScanner import Scanner
import grammar_productions as prod
from sys import exit


class Parser(object):

    def __init__(self, local_scanner):
        """Algorithm uses left most derivation to do the syntax analysis of the list of tokens from Scanner and outputs
        a parse tree."""
        self.local_scanner = local_scanner  # the Parser object is passed

    def _parse_error(self, match):
        """Function verifies the grammar of the string. If there is an error, the program is terminated."""
        if not match or match == 'ERROR':
            print(f'Syntax Error during Parsing: Invalid Grammar')
            exit(1)
        else:
            return

    def root(self):
        """root = operation"""
        first_element = self.local_scanner.peek()
        self._parse_error(first_element)
        if first_element == 'INTEGER':
            return self.parse_tree_operation()
        elif first_element == 'VARIABLE':
            return self.parse_variable_definition()

    def parse_tree_operation(self):
        first_element_parsed = self.parse_integer()
        operation = self.local_scanner.peek()
        self._parse_error(operation)
        if operation == 'PLUS':
            operation_parsed = self.parse_operator()
        second_element_parsed = self.parse_integer()
        equal_parsed = self.parse_equal()
        return prod.Operation(first_element_parsed, second_element_parsed, operation_parsed)

    def parse_variable_definition(self):
        first_element_parsed = self.parse_variable_name()
        equal = self.parse_equal()
        if self.local_scanner.peek() == 'VARIABLE':
            return self.parse_complex_variable_definition(first_element_parsed, equal)
        integer = self.parse_integer()

        return prod.VariableDefinition(first_element_parsed, equal, integer)

    def parse_complex_variable_definition(self, variable, equal):
        first_variable_name = self.parse_variable_name()
        plus = self.parse_operator()
        second_variable_name = self.parse_variable_name()
        return prod.ComplexVariableDefinition(variable, equal, first_variable_name, plus, second_variable_name)


    def parse_integer(self):
        integer = self.local_scanner.match('INTEGER')
        self._parse_error(integer)
        return prod.Integer(integer)

    def parse_variable_name(self):
        name_variable = self.local_scanner.match('VARIABLE')
        self._parse_error(name_variable)
        return prod.VariableName(name_variable)

    def parse_operator(self):
        operator_sign = self.local_scanner.match('PLUS')
        self._parse_error(operator_sign)
        return prod.Operator(operator_sign)

    def parse_equal(self):
        equal = self.local_scanner.match('EQUAL')
        self._parse_error(equal)
        return prod.Equal(equal)

    def main(self):
        result = []
        while not self.local_scanner.done():
            result.append(self.root())

        return result


class WorldState(object):

    def __init__(self):
        self.variables = {}




code = ["x = 10", "y = 11", "j = x + y", "1 + 2 ="]

TOKENS = [
            ((r"^[0-9]+"),                 "INTEGER"),
            ((r"^\+"),                     "PLUS"),
            ((r"\s"),                      "SPACE"),
            ((r"\="),                      "EQUAL"),
            ((r"[a-z]"),                   "VARIABLE")]

local_scanner = Scanner(TOKENS, code)
local_parser = Parser(local_scanner)
parse_tree = local_parser.main()
world_state = WorldState()
print(parse_tree)
local_analyzer = Analyzer(world_state)
analyzed_tree = local_analyzer.analyze()
for element in analyzed_tree:
    element.intrepret(world_state)
