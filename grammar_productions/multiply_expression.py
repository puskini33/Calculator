from grammar_productions.production import Production


class MultiplyExpression(Production):

    def __init__(self, left_number, right_number):
        self.left_number = left_number
        self.right_number = right_number

    def __repr__(self):
        return f'MultiplyExpression({self.left_number}, {self.right_number})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        multiplication = self.left_number.interpret(world_state) * self.right_number.interpret(world_state)
        print(multiplication)
        return multiplication
