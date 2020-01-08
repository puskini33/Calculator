from grammar_productions.production import Production
from string_scanner.scanner_string_segment import ScannedStringSegment


class Equal(Production):

    def __init__(self, equal_sign: ScannedStringSegment):
        self.equal = equal_sign.start_string

    def __repr__(self):
        return f'{self.equal}'

    def analyze(self, world_state):
        pass
