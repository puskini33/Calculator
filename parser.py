from scanner import Scanner
import grammar_productions as prod


class Parser(object):

    def __init__(self, local_parser):
        """Algorithm uses left most derivation to do the syntax analysis of the list of tokens from Scanner and outputs
        a parse tree."""
        self.local_scanner = local_scanner  # the Parser object is passed

    def root(self):
        """root = operation"""
        first_element = self.local_scanner.peek()
        if first_element == 'INTEGER':
            return self.parse_tree_operation()

    def parse_tree_operation(self):
        first_element_parsed = self.parse_integer()
        operation = self.local_scanner.peek()
        if operation == 'PLUS':
            operation_parsed = self.parse_operator()
        second_element_parsed = self.parse_integer()
        equal_parsed = self.parse_equal()
        return prod.Operation(first_element_parsed, second_element_parsed, operation_parsed, equal_parsed)

    def parse_integer(self):
        integer = self.local_scanner.match('INTEGER')
        return prod.Integer(integer)

    def parse_operator(self):
        operator_sign = self.local_scanner.match('PLUS')
        return prod.Operator(operator_sign)

    def parse_equal(self):
        equal = self.local_scanner.match('EQUAL')
        return prod.Equal(equal)

    def main(self):
        result = []
        # TODO: fix the code: the objects do not appear, only the list
        while not self.local_scanner.done():
            result.append(self.root())

        return result





code = ["1 + 2 ="]

TOKENS = [
            ((r"^[0-9]+"),                 "INTEGER"),
            ((r"^\+"),                     "PLUS"),
            ((r"\s"),                      "SPACE"),
            ((r"\="),                      "EQUAL")]

local_scanner = Scanner(TOKENS, code)
print(local_scanner)
local_parser = Parser(local_scanner)
print(local_parser.main())
