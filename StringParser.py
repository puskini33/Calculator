import grammar_productions as prod
from sys import exit


class Parser(object):

    def __init__(self, local_scanner):
        """Algorithm uses left most derivation to do the syntax analysis of the list of tokens from Scanner and outputs
        a parse tree."""
        self.local_scanner = local_scanner  # the Parser object is passed

    def parse(self):
        """Function parses the scanned tree and returns the parsed tree.
        root = parse_operation/ variable_definition"""
        result = []  # parse_tree
        first = self.local_scanner.peek().token

        while not self.local_scanner.done():
            if first == 'INTEGER':
                result.append(self.parse_operation(first))  # first_element to be parsed = INTEGER
            elif first == 'VARIABLE':
                second = self.local_scanner.peek().token
                if second == 'EQUAL':
                    result.append(self.parse_variable_definition())  # first_element to be parsed = EQUAL
                else:
                    result.append(self.parse_operation(first))  # first_element to be parsed = operation

        return result

    def _parse_error(self, match):
        """Function verifies the grammar of the string. If there is an error, the program is terminated."""
        if not match or match == 'ERROR':
            print(f'Syntax Error during Parsing: Invalid Grammar')
            exit(1)
        else:
            return

    def parse_variable_definition(self):
        variable = self.parse_variable_name()
        equal = self.parse_equal()
        integer = self.parse_integer()
        return prod.variable_definition.VariableDefinition(variable, equal, integer)

    def parse_operation(self, first_element_parsed):
        """operation = integer operator integer (equal)/ variable_symbol operator variable_symbol (equal)"""
        try:
            if first_element_parsed == 'INTEGER':
                operation_parsed = self.parse_integer_operation()
            elif first_element_parsed == 'VARIABLE':
                operation_parsed = self.parse_variable_operation()
        except UnboundLocalError:
            print('local variable operation_parsed referenced before assignment')

        return prod.operation.Operation(operation_parsed)  # TODO: See about the class Operation if sth. should be different there

    def parse_integer_operation(self):
        """integer operator integer (equal)"""
        first_element_parsed = self.parse_integer()
        operator = self.local_scanner.peek().token
        self._parse_error(operator)
        return self.evaluate_type_operation(operator, first_element_parsed)

    def parse_integer(self):
        """integer"""
        integer = self.local_scanner.match('INTEGER')
        self._parse_error(integer)
        return prod.integer.Integer(integer)

    def parse_variable_operation(self):
        """variable_symbol operator variable_symbol"""
        left_variable = self.parse_variable_name()
        operator = self.local_scanner.peek().token
        self._parse_error(operator)
        return self.evaluate_type_operation(operator, left_variable)

    def parse_variable_name(self):
        name_variable = self.local_scanner.match('VARIABLE')
        self._parse_error(name_variable)
        return prod.variable_name.VariableName(name_variable)

    def parse_equal(self):
        if self.local_scanner.peek().token == 'EQUAL':
            equal = self.local_scanner.match('EQUAL')
            self._parse_error(equal)
            return prod.equal.Equal(equal)
        elif self.local_scanner.peek().token != 'EQUAL':  # in case where there should be an equal there is another element
            print(f'Syntax Error during Parsing: Invalid Grammar')
            exit(1)
        else:
            return

    def evaluate_type_operation(self, operator, left_element):
        """integer operator integer (equal)"""
        if operator == 'MINUS':
            self.local_scanner.match('MINUS')
            right_element_peek = self.local_scanner.peek().token
            if right_element_peek == 'INTEGER':
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.subtract_expression.SubtractExpression(left_element, right_integer)
            elif right_element_peek == 'VARIABLE':
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.subtract_expression.SubtractExpression(left_element, right_variable)
        elif operator == 'PLUS':
            self.local_scanner.match('PLUS')
            right_element_peek = self.local_scanner.peek().token
            if right_element_peek == 'INTEGER':
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.add_expression.AddExpression(left_element, right_integer)
            elif right_element_peek == 'VARIABLE':
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.add_expression.AddExpression(left_element, right_variable)
        elif operator == 'DIVISION SIGN':
            self.local_scanner.match('DIVISION SIGN')
            right_element_peek = self.local_scanner.peek().token
            if right_element_peek == 'INTEGER':
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.divide_expression.DivideExpression(left_element, right_integer)
            elif right_element_peek == 'VARIABLE':
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.divide_expression.DivideExpression(left_element, right_variable)
        elif operator == 'TIMES SIGN':
            self.local_scanner.match('TIMES SIGN')
            right_element_peek = self.local_scanner.peek().token
            if right_element_peek == 'INTEGER':
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.multiply_expression.MultiplyExpression(left_element, right_integer)
            elif right_element_peek == 'VARIABLE':
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.multiply_expression.MultiplyExpression(left_element, right_variable)
        elif operator == 'MODULO SIGN':
            self.local_scanner.match('MODULO SIGN')
            right_element_peek = self.local_scanner.peek().token
            if right_element_peek == 'INTEGER':
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.modulo_expression.ModuloExpression(left_element, right_integer)
            elif right_element_peek == 'VARIABLE':
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.modulo_expression.ModuloExpression(left_element, right_variable)
        else:  # This else is here to catch the wrong grammar in the syntax: 1 1 + 1 =
            print(f'Syntax Error during Parsing: Invalid Grammar')
            exit(1)
