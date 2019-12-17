class Analyze(object):

    def __init__(self, parse_tree):
        self.parse_tree = parse_tree

    def analyze(self):
        for element in parse_tree:
            element.analyze()

        return self.parse_tree
