class Production(object):

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        pass


class Operation(Production):

    def __init__(self, type_operation):
        self.type_operation = type_operation

    def __repr__(self):
        return f'Operation({self.type_operation})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        return self.type_operation.interpret(world_state)


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


class SubtractExpression(Production):

    def __init__(self, left_number, right_number):
        self.left_number = left_number  # 'MINUS'
        self.right_number = right_number

    def __repr__(self):
        return f'SubtractExpression({self.left_number}, {self.right_number})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        substraction = self.left_number.interpret(world_state) - self.right_number.interpret(world_state)
        print(substraction)
        return substraction


class AddExpression(Production):

    def __init__(self, left_number, right_number):
        self.left_number = left_number
        self.right_number = right_number

    def __repr__(self):
        return f'AddExpression({self.left_number}, {self.right_number})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        addition = self.left_number.interpret(world_state) + self.right_number.interpret(world_state)
        print(addition)
        return addition


class DivideExpression(Production):

    def __init__(self, left_number, right_number):
        self.left_number = left_number
        self.right_number = right_number

    def __repr__(self):
        return f'DivideExpression({self.left_number}, {self.right_number})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        division = self.left_number.interpret(world_state) / self.right_number.interpret(world_state)
        print(division)
        return division


class MultiplyExpression(Production):

    def __init__(self, left_number, right_number):
        self.left_number = left_number
        self.right_number = right_number

    def __repr__(self):
        return f'MultiplyExpression({self.left_number}, {self.right_number})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        multiplication = self.left_number.interpret(world_state) * self.right_number.interpret(world_state)
        print(multiplication)
        return multiplication


class ModuloExpression(Production):

    def __init__(self, left_number, right_number):
        self.left_number = left_number
        self.right_number = right_number

    def __repr__(self):
        return f'ModuloExpression({self.left_number}, {self.right_number})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        modulo = self.left_number.interpret(world_state) % self.right_number.interpret(world_state)
        print(modulo)
        return modulo


class Equal(Production):

    def __init__(self, equal_sign):
        self.equal = equal_sign[1]

    def __repr__(self):
        return f'{self.equal}'

    def analyze(self, world_state):
        pass
