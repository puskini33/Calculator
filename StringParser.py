import grammar_productions as prod

from sys import exit


class Parser(object):

    def __init__(self, local_scanner):
        """Algorithm uses left most derivation to do the syntax analysis of the list of tokens from Scanner and outputs
        a parse tree."""
        self.local_scanner = local_scanner  # the Parser object is passed

    def parse(self):
        """Function parses the scanned tree and returns the parsed tree."""
        result = []  # parse_tree
        while not self.local_scanner.done():  # TODO: ask whether the while loops because the function returns True or False
            result.append(self.parse_operation())

        return result

    def _parse_error(self, match):
        """Function verifies the grammar of the string. If there is an error, the program is terminated."""
        if not match or match == 'ERROR':
            print(f'Syntax Error during Parsing: Invalid Grammar')
            exit(1)
        else:
            return

    def parse_operation(self):
        """operation = integer operator integer (equal)/ variable_symbol operator variable_symbol"""
        first_element_parsed = self.local_scanner.peek()

        if first_element_parsed == 'INTEGER':
            operation_parsed = self.parse_integer_operation()
        elif first_element_parsed == 'VARIABLE':
            operation_parsed = self.parse_variable_operation()

        return prod.Operation(operation_parsed)  # TODO: See about the class Operation if sth. should be different there

    def parse_integer_operation(self):
        """integer operator integer (equal)"""
        first_element_parsed = self.parse_integer()
        operator = self.local_scanner.peek()
        self._parse_error(operator)
        return self.evaluate_type_operation(operator, first_element_parsed)

    def parse_integer(self):
        """integer"""
        integer = self.local_scanner.match('INTEGER')
        self._parse_error(integer)
        return prod.Integer(integer)

    def parse_variable_operation(self):
        """variable_symbol operator variable_symbol"""
        left_variable = self.parse_variable_name()
        operator = self.local_scanner.peek()
        self._parse_error(operator)
        return self.evaluate_type_operation(operator, left_variable)

    def parse_variable_name(self):
        name_variable = self.local_scanner.match('VARIABLE')
        self._parse_error(name_variable)
        return prod.VariableName(name_variable)

    def evaluate_type_operation(self, operator, left_element):
        """integer operator integer (equal)"""
        if operator == 'MINUS':
            operator_sign = self.local_scanner.match('MINUS')
            right_element_peek = self.local_scanner.peek()
            if right_element_peek == 'INTEGER':
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.SubtractExpression(left_element, right_integer)
            elif right_element_peek == 'VARIABLE':
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.SubtractExpression(left_element, right_variable)
        elif operator == 'PLUS':
            operator_sign = self.local_scanner.match('PLUS')
            right_element_peek = self.local_scanner.peek()
            if right_element_peek == 'INTEGER':
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.AddExpression(left_element, right_integer)
            elif right_element_peek == 'VARIABLE':
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.AddExpression(left_element, right_variable)
        elif operator == 'DIVISION SIGN':
            operator_sign = self.local_scanner.match('DIVISION SIGN')
            right_element_peek = self.local_scanner.peek()
            if right_element_peek == 'INTEGER':
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.DivideExpression(left_element, right_integer)
            elif right_element_peek == 'VARIABLE':
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.DivideExpression(left_element, right_variable)
        elif operator == 'TIMES SIGN':
            operator_sign = self.local_scanner.match('TIMES SIGN')
            right_element_peek = self.local_scanner.peek()
            if right_element_peek == 'INTEGER':
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.MultiplyExpression(left_element, right_integer)
            elif right_element_peek == 'VARIABLE':
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.MultiplyExpression(left_element, right_variable)
        elif operator == 'MODULO SIGN':
            operator_sign = self.local_scanner.match('MODULO SIGN')
            right_element_peek = self.local_scanner.peek()
            if right_element_peek == 'INTEGER':
                right_integer = self.parse_integer()
                self.parse_equal()
                return prod.ModuloExpression(left_element, right_integer)
            elif right_element_peek == 'VARIABLE':
                right_variable = self.parse_variable_name()
                self.parse_equal()
                return prod.ModuloExpression(left_element, right_variable)

    def parse_variable_definition(self):
        first_element_parsed = self.parse_variable_name()
        equal = self.parse_equal()
        if self.local_scanner.peek() == 'VARIABLE':
            return self.parse_complex_variable_definition(first_element_parsed, equal)
        integer = self.parse_integer()

        return prod.VariableDefinition(first_element_parsed, equal, integer)

    def parse_equal(self):
        if self.local_scanner.peek() == 'EQUAL':
            equal = self.local_scanner.match('EQUAL')
            self._parse_error(equal)
            return prod.Equal(equal)
        else:
            return
