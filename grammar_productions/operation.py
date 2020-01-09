from grammar_productions.production import Production


class Operation(Production):

    def __init__(self, type_operation):
        self.type_operation = type_operation

    def __repr__(self):
        return f'Operation({self.type_operation})'

    def analyze(self, world_state):
        self.type_operation.analyze(world_state)

    def interpret(self, world_state):
        return self.type_operation.interpret(world_state)
