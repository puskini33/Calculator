from grammar_productions.production import Production


class VariableDefinition(Production):

    def __init__(self, name, equal, number):
        self.name = name
        self.equal = equal
        self.number = number

    def __repr__(self):
        return f'VariableDefinition({self.name} {self.equal} {self.number})'

    def analyze(self, world_state):
        world_state.variables[self.name] = self

    def interpret(self, world_state):
        pass
