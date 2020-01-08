from grammar_productions.production import Production
from string_scanner.scanner_string_segment import ScannedStringSegment


class Operation(Production):

    def __init__(self, type_operation: ScannedStringSegment):
        self.type_operation = type_operation.start_string

    def __repr__(self):
        return f'Operation({self.type_operation})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        return self.type_operation.interpret(world_state)
