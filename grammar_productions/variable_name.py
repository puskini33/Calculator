from grammar_productions.production import Production
from string_scanner.scanner_string_segment import ScannedStringSegment


class VariableName(Production):

    def __init__(self, name: ScannedStringSegment):
        self.name = name.start_string

    def __repr__(self):
        return f'Variable({self.name})'

    def analyze(self, world_state):
        world_state.variables[self.name] = self
