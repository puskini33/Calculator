from grammar_productions.production import Production
from string_scanner.scanner_string_segment import ScannedStringSegment


class Integer(Production):

    def __init__(self, element: ScannedStringSegment):
        self.element = int(element.start_string)

    def __repr__(self):
        return f'Integer({self.element})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        return self.element
