class Interpreter(object):

    def __init__(self, analyzed_tree):
        self.analyzed_tree = analyzed_tree

    def interpret(self, world_state):
        for element in self.analyzed_tree:
            element.interpret(world_state)
