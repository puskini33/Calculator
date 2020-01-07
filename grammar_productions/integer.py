from grammar_productions.production import Production


class Integer(Production):

    def __init__(self, element):
        self.element = int(element[1])

    def __repr__(self):
        return f'Integer({self.element})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        return self.element
