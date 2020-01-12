from grammar_productions.production import Production
from string_scanner.scanner_string_segment import ScannedStringSegment
from world_state import WorldState


class VariableName(Production):

    def __init__(self, name: ScannedStringSegment):
        self.name = name.start_string

    def __repr__(self):
        return f'Variable({self.name})'

    def analyze(self, world_state: WorldState):
        pass

    def interpret(self, world_state: WorldState):
        ref = world_state.variables.get(self.name)  # Int()
        print(ref)
        return ref.interpret(world_state)
