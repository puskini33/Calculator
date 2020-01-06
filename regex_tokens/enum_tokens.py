from enum import Enum


class TokenName(Enum):  # TODO: Could I add new values to this class?
    integer = 'INTEGER'
    plus = 'PLUS'
    variable = 'VARIABLE'
    equal = 'EQUAL'
    minus = 'MINUS'
    division_sign = 'DIVISION SIGN'
    times_sign = 'TIMES SIGN'
    modulo_sign = 'MODULO SIGN'
    space = 'SPACE'
