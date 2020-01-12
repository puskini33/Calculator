from grammar_productions.production import Production


class VariableDefinition(Production):

    def __init__(self, object_name, equal, number):
        self.object_name = object_name
        self.equal = equal
        self.number = number

    def __repr__(self):
        return f'VariableDefinition({self.object_name} {self.equal} {self.number})'

    def analyze(self, world_state):
        world_state.variables[self.object_name.name] = self.number

    def interpret(self, world_state):
        ref = world_state.variables.get(self.object_name.name)
        return ref.interpret(world_state)
