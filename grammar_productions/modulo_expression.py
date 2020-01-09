from grammar_productions.production import Production


class ModuloExpression(Production):

    def __init__(self, left_number, right_number):
        self.left_number = left_number
        self.right_number = right_number

    def __repr__(self):
        return f'ModuloExpression({self.left_number}, {self.right_number})'

    def analyze(self, world_state):
        self.left_number.analyze(world_state)
        self.right_number.analyze(world_state)

    def interpret(self, world_state):
        modulo = self.left_number.interpret(world_state) % self.right_number.interpret(world_state)
        print(modulo)
        return modulo
