from math import sqrt

from utilities.maths import Number


def solve_second_degree(a, b, c):
    if type(a) == tuple or type(a) == list:
        a = a[0]
    if type(a) == str:
        try:
            a = int(a)
        except ValueError:
            return None
    elif type(a) != int and type(a) != float and type(a) != Number:
        return None

    if type(b) == tuple or type(a) == list:
        b = b[0]
    if type(b) == str:
        try:
            b = int(b)
        except ValueError:
            return None
    elif type(b) != int and type(b) != float and type(b) != Number:
        return None

    if type(c) == tuple or type(c) == list:
        c = c[0]
    if type(c) == str:
        try:
            c = int(c)
        except ValueError:
            return None
    elif type(c) != int and type(c) != float and type(c) != Number:
        return None
    
    return ((-b + sqrt((b**2)-4*a*c))/2*a), ((-b - sqrt((b**2)-4*a*c))/2*a)


def solve(*args):
    pass
