from grammar_productions.production import Production
from world_state import WorldState
from grammar_productions.integer import Integer
from grammar_productions.variable_name import VariableName


class AddExpression(Production):

    def __init__(self, left_element: Integer or VariableName, right_element: Integer or VariableName):
        self.left_element = left_element
        self.right_element = right_element

    def __repr__(self):
        return f'AddExpression({self.left_element}, {self.right_element})'

    def analyze(self, world_state: WorldState):
        self.left_element.analyze(world_state)
        self.right_element.analyze(world_state)

    def call(self, world_state):
        pass

    def interpret(self, world_state: WorldState):
        if type(self.left_element) == Integer:
            addition = self.left_element.interpret(world_state) + self.right_element.interpret(world_state)
            print(addition)
            return addition
        else:
            integer_object_left = world_state.variables.get(self.left_element.name)
            integer_left = integer_object_left.interpret(world_state)
            integer_object_right = world_state.variables.get(self.right_element.name)
            integer_right = integer_object_right.interpret(world_state)
            print(integer_left + integer_right)
            return integer_left + integer_right
