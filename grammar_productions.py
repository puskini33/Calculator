class Production(object):

    def analyze(self):
        pass


class Operation(Production):

    def __init__(self, first_element, second_element, operator, equal):
        self.first_element = first_element
        self.second_element = second_element
        self.operator = operator
        self.equal = equal

    def __repr__(self):
        return f'{self.first_element} {self.operator} {self.second_element} {self.equal}'

    def analyze(self):
        pass

class Integer(Production):

    def __init__(self, element):
        self.element = element

    def __repr__(self):
        return f'{self.element}'


class Operator(Production):

    def __init__(self, type_operator):
        self.type_operator = type_operator

    def __repr__(self):
        return f'{self.type_operator}'


class Equal(Production):

    def __init__(self, equal_sign):
        self.equal = equal_sign

    def __repr__(self):
        return f'{self.equal}'
