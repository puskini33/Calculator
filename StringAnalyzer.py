class Analyzer(object):

    def __init__(self, parse_tree):
        self.parse_tree = parse_tree

    def analyze(self, world_state):
        for element in self.parse_tree:
            element.analyze(world_state)

        return self.parse_tree
