from StringScanner import Scanner
from StringAnalyzer import Analyzer
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
        """root = operation/ variable_definition"""
        first_element = self.local_scanner.peek()
        self._parse_error(first_element)
        if first_element == 'INTEGER':
            return self.parse_tree_operation()
        elif first_element == 'VARIABLE':
            return self.parse_variable_definition()

    def parse_tree_operation(self):
        """operation = integer operation integer"""
        first_element_parsed = self.parse_integer()
        operator = self.local_scanner.peek()
        self._parse_error(operator)
        operation_parsed = self.parse_operation(first_element_parsed)
        return prod.Operation(operation_parsed)

    def parse_variable_definition(self):
        first_element_parsed = self.parse_variable_name()
        equal = self.parse_equal()
        if self.local_scanner.peek() == 'VARIABLE':
            return self.parse_complex_variable_definition(first_element_parsed, equal)
        integer = self.parse_integer()

        return prod.VariableDefinition(first_element_parsed, equal, integer)

    def parse_complex_variable_definition(self, variable, equal):
        first_variable_name = self.parse_variable_name()
        # plus = self.parse_operation()
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

    def parse_operation(self, left_number):
        peek_operator_sign = self.local_scanner.peek()
        self._parse_error(peek_operator_sign)
        print(peek_operator_sign)

        if peek_operator_sign == 'MINUS':
            operator_sign = self.local_scanner.match('MINUS')
            right_number = self.parse_integer()
            self.parse_equal()
            return prod.SubtractExpression(left_number, right_number)
        elif peek_operator_sign == 'PLUS':
            operator_sign = self.local_scanner.match('PLUS')
            right_number = self.parse_integer()
            self.parse_equal()
            return prod.AddExpression(left_number, right_number)
        elif peek_operator_sign == 'DIVISION SIGN':
            operator_sign = self.local_scanner.match('DIVISION SIGN')
            right_number = self.parse_integer()
            self.parse_equal()
            return prod.DivideExpression(left_number, right_number)
        elif peek_operator_sign == 'TIMES SIGN':
            operator_sign = self.local_scanner.match('TIMES SIGN')
            right_number = self.parse_integer()
            self.parse_equal()
            return prod.MultiplyExpression(left_number, right_number)
        elif peek_operator_sign == 'MODULO SIGN':
            operator_sign = self.local_scanner.match('MODULO SIGN')
            right_number = self.parse_integer()
            self.parse_equal()
            return prod.ModuloExpression(left_number, right_number)

    def parse_equal(self):
        equal = self.local_scanner.match('EQUAL')
        self._parse_error(equal)
        return prod.Equal(equal)
