from grammar_productions.production import Production
from grammar_productions.integer import Integer


class ModuloExpression(Production):

    def __init__(self, left_element, right_element):
        self.left_element = left_element
        self.right_element = right_element

    def __repr__(self):
        return f'ModuloExpression({self.left_element}, {self.right_element})'

    def analyze(self, world_state):
        self.left_element.analyze(world_state)
        self.right_element.analyze(world_state)

    def interpret(self, world_state):
        if type(self.left_element) == Integer:
            modulo = self.left_element.interpret(world_state) % self.right_element.interpret(world_state)
            print(modulo)
            return modulo
        else:
            integer_object_left = world_state.variables.get(self.left_element.name)
            integer_left = integer_object_left.interpret(world_state)
            integer_object_right = world_state.variables.get(self.right_element.name)
            integer_right = integer_object_right.interpret(world_state)
            print(integer_left % integer_right)
            return integer_left % integer_right

