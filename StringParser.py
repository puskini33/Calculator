from regex_tokens.enum_tokens import TokenName
from string_scanner.scanner_string_segment import ScannedStringSegment
import grammar_productions as prod
from sys import exit


class Parser(object):

    def __init__(self, local_scanner):
        """Algorithm uses left most derivation to do the syntax analysis of the list of tokens from Scanner and outputs
        a parse tree."""
        self.local_scanner = local_scanner

    def parse(self) -> list:
        """Function parses the scanned tree and returns the parsed tree.
        root = parse_operation/ variable_definition"""
        try:
            result = []  # parse_tree

            while not self.local_scanner.done():
                first = self.local_scanner.peek().token
                if first == TokenName.integer.value:
                    result.append(self.parse_integer_operation())  # first_element to be parsed = INTEGER
                elif first == TokenName.variable.value:
                    first = self.parse_variable_name()
                    second = self.local_scanner.peek().token
                    if second == TokenName.equal.value:
                        result.append(self.parse_variable_definition(first))  # first_element to be parsed = EQUAL
                    else:
                        result.append(self.parse_variable_operation(first))  # first_element to be parsed = operation

            return result
        except AttributeError:
            print('Attribute Error during Parsing: Invalid Grammar.')
            exit(1)

    def _parse_error(self, match: str):
        """Function verifies the grammar of the string. If there is an error, the program is terminated."""
        if not match:
            print('Syntax Error during Parsing: Invalid Grammar')
            exit(1)
        else:
            return

    def parse_integer_operation(self) -> prod.operation.Operation:
        """integer operator integer (equal)"""
        first_element_parsed = self.parse_integer()
        operator = self.local_scanner.peek().token
        self._parse_error(operator)
        type_operation = self.evaluate_type_operation(operator, first_element_parsed)
        return prod.operation.Operation(type_operation)

    def parse_integer(self) -> prod.integer.Integer:
        """integer"""
        integer = self.local_scanner.match(TokenName.integer.value)
        self._parse_error(integer)
        return prod.integer.Integer(integer)

    def parse_variable_operation(self, left_variable: prod.variable_name.VariableName) -> prod.operation.Operation:
        """variable_symbol operator variable_symbol"""
        operator = self.local_scanner.peek().token
        self._parse_error(operator)
        type_operation = self.evaluate_type_operation(operator, left_variable)
        return prod.operation.Operation(type_operation)

    def parse_variable_definition(self, variable: prod.variable_name.VariableName) -> prod.variable_definition.VariableDefinition:
        """variable_name equal integer"""
        equal = self.parse_equal()
        integer = self.parse_integer()
        return prod.variable_definition.VariableDefinition(variable, equal, integer)

    def parse_variable_name(self) -> prod.variable_name.VariableName:
        """variable_name"""
        name_variable = self.local_scanner.match(TokenName.variable.value)
        self._parse_error(name_variable)
        return prod.variable_name.VariableName(name_variable)

    def parse_equal(self) -> prod.equal.Equal or None:
        """equal"""
        if self.local_scanner.peek().token == TokenName.equal.value:
            equal = self.local_scanner.match(TokenName.equal.value)
            self._parse_error(equal)
            self.local_scanner.parse_extra_space()
            return prod.equal.Equal(equal)
        elif self.local_scanner.peek().token != TokenName.equal.value:  # in the case when there should be an equal there is another element
            print('Syntax Error during Parsing: Invalid Grammar')
            exit(1)
        else:
            return

    def evaluate_type_operation(self, operator: ScannedStringSegment, left_element: prod.variable_name.VariableName or prod.integer.Integer):
        """integer operator integer (equal)"""
        if operator == TokenName.minus.value:
            self.local_scanner.match(TokenName.minus.value)
            right_element_peek = self.local_scanner.peek().token
            if right_element_peek == TokenName.integer.value:
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.subtract_expression.SubtractExpression(left_element, right_integer)
            elif right_element_peek == TokenName.variable.value:
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.subtract_expression.SubtractExpression(left_element, right_variable)
        elif operator == TokenName.plus.value:
            self.local_scanner.match(TokenName.plus.value)
            right_element_peek = self.local_scanner.peek().token
            if right_element_peek == TokenName.integer.value:
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.add_expression.AddExpression(left_element, right_integer)
            elif right_element_peek == TokenName.variable.value:
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.add_expression.AddExpression(left_element, right_variable)
        elif operator == TokenName.division_sign.value:
            self.local_scanner.match(TokenName.division_sign.value)
            right_element_peek = self.local_scanner.peek().token
            if right_element_peek == TokenName.integer.value:
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.divide_expression.DivideExpression(left_element, right_integer)
            elif right_element_peek == TokenName.variable.value:
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.divide_expression.DivideExpression(left_element, right_variable)
        elif operator == TokenName.times_sign.value:
            self.local_scanner.match(TokenName.times_sign.value)
            right_element_peek = self.local_scanner.peek().token
            if right_element_peek == TokenName.integer.value:
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.multiply_expression.MultiplyExpression(left_element, right_integer)
            elif right_element_peek == TokenName.variable.value:
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.multiply_expression.MultiplyExpression(left_element, right_variable)
        elif operator == TokenName.modulo_sign.value:
            self.local_scanner.match(TokenName.modulo_sign.value)
            right_element_peek = self.local_scanner.peek().token
            if right_element_peek == TokenName.integer.value:
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.modulo_expression.ModuloExpression(left_element, right_integer)
            elif right_element_peek == TokenName.variable.value:
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.modulo_expression.ModuloExpression(left_element, right_variable)
        else:  # This else is here to catch the wrong grammar in the syntax: 1 1 + 1 =
            print('Syntax Error during Parsing: Invalid Grammar')
            exit(1)
