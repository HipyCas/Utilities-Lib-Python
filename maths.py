"""
Some mathematic utilities, including functions and useful classes
"""


prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                 991]
prime_numbers_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


class Number:

    def __init__(self, value=0):
        self.value = value
        self.values = []

    def add(self, number):
        self.value += number

    def quit(self, number):
        self.value -= number

    def multiply(self, number):
        self.value *= number

    def elevate(self, number):
        self.value = self.value ** number

    def divide(self, number, save_int=True):
        self.value /= number
        if save_int:
            self.value = int(self.value)

    def divide_int(self, number, save_int=True):
        self.value = self.value // number
        if save_int:
            self.value = int(self.value)

    def module(self, number, save_int=True):
        self.value %= number
        if save_int:
            self.value = int(self.value)

    def make_int(self):
        self.value = int(self.value)

    def make_float(self):
        self.value = float(self.value)

    def make_str(self):
        self.value = str(self.value)

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return str(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        return self.value / other

    def __floordiv__(self, other):
        return self.value // other

    def __mod__(self, other):
        return self.value % other

    def __pow__(self, power, modulo=None):
        return self.value ** power

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def __len__(self):
        return len(str(self.value))

    def __getitem__(self, item):
        return str(self.value)[item]

    def __iter__(self):
        return iter(self.values)

    def __contains__(self, item):
        return item in self.values


def square(x):
    """
    Returns the number x elevated to 2
    :param x:
    :return:
    """
    return x ** 2


def cube(x):
    """
    Returns the number x elevated to 3
    :param x:
    :return:
    """
    return x ** 3


def quad(x):
    """
    Returns the number x elevated to 4
    :param x:
    :return:
    """
    return x ** 4


def isEven(x):
    """
    Returns True if number x is even
    :param x:
    :return:
    """
    if x % 2 == 0:
        return True
    else:
        return False


def isOdd(x):
    """
    Returns True if number x is odd
    :param x:
    :return:
    """
    if x % 2 == 0:
        return False
    else:
        return True


def factorize(x):
    factors = []
    for prime in prime_numbers_100:
        calculating = True
        while calculating:
            if x % prime == 0:
                factors.append(prime)
                x = int(x / prime)
            else:
                break
        if x == 1:
            break
    if x != 1:
        factors.append(x)
    return factors


def factorize_precision(x):
    factors = []
    for prime in prime_numbers:
        calculating = True
        while calculating:
            if x % prime == 0:
                factors.append(prime)
                x /= prime
            else:
                break
        if x == 1:
            break
    if x != 1:
        factors.append(x)
    return factors


def round(num: float):
    if (num - int(num)) >= 0.5:
        num += 1
    return int(num)
