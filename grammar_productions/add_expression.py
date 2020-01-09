from grammar_productions.production import Production
from world_state import WorldState
from grammar_productions.integer import Integer
from grammar_productions.variable_name import VariableName
from string_scanner.scanner_string_segment import ScannedStringSegment


class AddExpression(Production):

    def __init__(self, left_element: Integer or VariableName, right_element: Integer or VariableName):
        self.left_element = left_element
        self.right_element = right_element

    def __repr__(self):
        return f'AddExpression({self.left_element}, {self.right_element})'

    def analyze(self, world_state: WorldState):
        self.left_element.analyze(world_state)
        self.right_element.analyze(world_state)

    def interpret(self, world_state: WorldState):
        if type(self.left_element) == Integer:
            addition = self.left_element.interpret(world_state) + self.right_element.interpret(world_state)
            print(addition)
            return addition
        else:
            left_variable = world_state.variables.get(self.left_element)  # VariableDefinition
            right_variable = world_state.variables.get(self.right_element)  # VariableDefinition
            left_variable.call(world_state, integer)
            print(left_variable)
            addition = left_variable.number.element + right_variable.number.element
            print(addition)
            return addition
