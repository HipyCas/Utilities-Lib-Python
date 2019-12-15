class Atom:
    count = 0

    def __init__(self, usePreset=False, **kwargs):
        if usePreset:
            preset = kwargs['preset']
            self.z = preset.z
            self.a = preset.a
            self.m = preset.m
            self.p = preset.p

        else:
            self.z = kwargs['z']
            self.a = kwargs['a']


class PeriodicTableElement:
    count = 0

    def __init__(self, nick):
        self.nick = str(nick)
        self.count += 1


class Hydrogen (PeriodicTableElement):
    count: int = 0
    name = "Hydrogen"
    symbol = "H"
    z = 1
    a = 1
    m: float = 1.00794
    p = 1
    n = 0
    e = 1

    def __init__(self, nick):
        self.nick = str(nick)
        self.count += 1

    def __add__(self, other):
        if type(other) == Hydrogen:
            return Helium(self.nick + " + " + other.nick)


class Helium(PeriodicTableElement):
    count = 0
    name = "Helium"
    symbol = "He"
    z = 2
    a = 4
    m = 4.002602
    p = 2
    n = 2
    e = 2

    def __init__(self, nick):
        self.nick = str(nick)
        self.count += 1


class Lithium (PeriodicTableElement):
    name = "Lithium"
    symbol = "Li"
    z = 3
    a = 7
    m = 6.941
    p = 3
    n = 4
    e = 3

    def __init__(self, nick):
        self.nick = str(nick)
        self.count += 1


class Beryllium (PeriodicTableElement):
    name = "Beryllium"
    symbol = "Be"
    z = 4
    a = 9
    m = 9.0121
    p = 4
    n = 5
    e = 4

    def __init__(self, nick):
        self.nick = str(nick)
        self.count += 1