import random
from math import sin, cos, tan, pi, atan, cosh, sinh, e

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

def random_func():
    funcs = [sin, cos, tan, sinh, cosh]
    r_func = random.choice(funcs)
    return r_func

def r_one(x, y):
    return tan(sin(x) * pi * e)

def r_two(x, y):
    return sin(pi * x) * e

def r_three(x, y):
    return cos(pi * x * y)

def r_four(x, y):
    return sin(pi * y) * x

def r_five(x, y):
    output = sin(e * pi * cos(pi * sin(e * pi * cos(pi * cos(e * pi * y) * x)) * sin(pi * y)))
    return output

def r_six(x, y):
    output = abs((sin(x ** 2 + pi) - cos(y ** 2 + pi))) ** 0.5
    return output

def r_seven(x, y):
    output = (cos(x * pi) - cos(y * pi)) * e
    return output

def r_eight(x, y):
    output = (tan(x ** 2) - tan(y ** 2))
    return output

def r_nine(x, y):
    return sin(x * y * pi * e) - cos(x * y * pi * e)

def r_ten(x, y):
    return sin(pi * x) * cos(pi * y) * tan(x * y * pi)

def r_eleven(x, y):
    return tan(pi * cos(pi * sin(pi * cos(pi * cos(pi * y) * x)) * sin(pi * y)))

def r_twelve(x, y):
    return tan(pi * cos(pi * sin(pi * cos(pi * y))) * sin(pi * cos(pi * x) * y) * cos(pi * sin(pi * x)))

def r_thirteen(x, y):
    return tan(sin(pi * x * sin(pi * y * cos(pi * x * cos(pi * y ** 3)))) ** 2 - cos(e * y * cos(e * x * sin(e * y * sin(e * x ** 3)))) ** 2)

def r_fourteen(x, y):
    return sin(pi * cos(pi * sin(pi * cos(pi * sin(pi * tan(x ** 2 + pi) * e * 10) - tan(x * y) * pi))) + sin(pi * cos(pi * sin(pi * cos(pi * tan(y ** 2 + pi) * cosh(x * y) ** 3)))))

def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr = random.choice([r_one, r_two, r_three, r_four, r_five, r_six, r_seven, r_eight, r_nine, r_ten, r_eleven, r_twelve, r_thirteen, r_fourteen])
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
