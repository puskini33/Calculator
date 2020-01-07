from grammar_productions.production import Production


class Equal(Production):

    def __init__(self, equal_sign):
        self.equal = equal_sign[1]

    def __repr__(self):
        return f'{self.equal}'

    def analyze(self, world_state):
        pass
