class Production(object):

    def analyze(self, world_state):
        pass


class Operation(Production):

    def __init__(self, first_element, second_element, operator):
        self.first_element = first_element
        self.second_element = second_element
        self.operator = operator

    def __repr__(self):
        return f'Operation({self.first_element} {self.operator} {self.second_element})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        left = self.first_element.interpret(world_state)
        right = self.second_element.interpret(world_state)
        operator = self.operator.interpret(world_state)
        return self.calculate(left, right, operator)

    def calculate(self, left, right, operator):
        if operator == 'add':
            addition = left + right
            return left + right

class VariableDefinition(Production):

    def __init__(self, name, equal, number):
        self.name = name
        self.equal = equal
        self.number = number

    def __repr__(self):
        return f'VariableDefinition({self.name}{self.equal}{self.number})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        pass


class ComplexVariableDefinition(Production):

    def __init__(self, name, equal, first_variable, plus, second_variable):
        self.name = name
        self.equal = equal
        self.first_variable = first_variable
        self.plus = plus
        self.second_variable = second_variable

    def __repr__(self):
        return f'VariableDefinition({self.name}{self.equal}{self.first_variable}{self.plus}{self.second_variable})'

    def analyze(self, world_state):
        self.first_variable.analyze(world_state)
        self.second_variable.analyze(world_state)
        self.name.analyze(world_state)


class Integer(Production):

    def __init__(self, element):
        self.element = int(element[1])

    def __repr__(self):
        return f'Integer({self.element})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        return self.element


class VariableName(Production):

    def __init__(self, name):
        self.name = name[1]

    def __repr__(self):
        return f'Variable({self.name})'

    def analyze(self, world_state):
        world_state.variables[self.name] = self


class Plus(Production):

    def __init__(self, type_operator):
        self.type_operator = type_operator[1]

    def __repr__(self):
        return f'{self.type_operator}'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        return 'add'


class Equal(Production):

    def __init__(self, equal_sign):
        self.equal = equal_sign[1]

    def __repr__(self):
        return f'{self.equal}'

    def analyze(self, world_state):
        pass
