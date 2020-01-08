from grammar_productions.production import Production
from string_scanner.scanner_string_segment import ScannedStringSegment


class AddExpression(Production):

    def __init__(self, left_number, right_number):
        self.left_number = left_number
        self.right_number = right_number

    def __repr__(self):
        return f'AddExpression({self.left_number}, {self.right_number})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        addition = self.left_number.interpret(world_state) + self.right_number.interpret(world_state)
        print(addition)
        return addition
