from grammar_productions.production import Production


class VariableName(Production):

    def __init__(self, name):
        self.name = name[1]

    def __repr__(self):
        return f'Variable({self.name})'

    def analyze(self, world_state):
        world_state.variables[self.name] = self
