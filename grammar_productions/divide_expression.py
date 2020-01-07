from grammar_productions.production import Production


class DivideExpression(Production):

    def __init__(self, left_number, right_number):
        self.left_number = left_number
        self.right_number = right_number

    def __repr__(self):
        return f'DivideExpression({self.left_number}, {self.right_number})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        division = self.left_number.interpret(world_state) / self.right_number.interpret(world_state)
        print(division)
        return division
