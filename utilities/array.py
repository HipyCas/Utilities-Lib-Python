class Array:

    def __init__(self, *args):
        self.list = list(args)
        self.tuple = tuple(args)
        self.default = 0
        self.lastpop = None

    def set_default(self, default="0"):
        if str(default) == "0" or str(default).upper() == "LIST" or str(default).upper() == "LISTA":
            self.default = 0
            return True
        elif str(default) == "1" or str(default) == "tuple" or str(default) == "Tuple" or str(default) == "TUPLE" or str(default) == "tupla":
            self.default = 1
            return True
        else:
            print("Invalid type")
            return False

    def pop(self, index=-1):
        del self.tuple
        self.lastpop = self.list.pop(index)
        self.tuple = tuple(self.list)
        return self.lastpop

    def pop_only(self, index=-1):
        if self.default == 0:
            self.lastpop = self.list.pop(index)
            return self.lastpop
        elif self.default == 1:
            if self.tuple == tuple(self.list):
                del self.tuple
                self.lastpop = self.list.pop(index)
                self.tuple = tuple(self.list)
                self.list.insert(index, self.lastpop)
                return self.lastpop
            else:
                raise DeprecationWarning

    def __reversed__(self):
        self.list = reversed(self.list)
        self.tuple = reversed(self.tuple)

        if self.default == 0:
            return self.list
        elif self.default == 1:
            return self.tuple

    def __getitem__(self, item):
        if self.default == 0:
            return self.list[item]
        elif self.default == 1:
            return self.tuple[item]

    def __add__(self, other):
        if type(other) == list:
            return self.list + other
        elif type(other) == tuple:
            return self.tuple + other

    def __sub__(self, other):
        if type(other) == list:
            return self.list + other
        elif type(other) == tuple:
            return self.tuple + other


if __name__ == '__main__':
    a = Array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(a.tuple)
    print(a.list)
    print(a.pop())
    print(a.tuple)
    print(a.list)
    print(a.pop_only())
    print(a.tuple)
    print(a.list)
    a.set_default(1)
    print(a.tuple)
    print(a.list)
    print("-----")
    print(a.pop_only(1))
    print(a.tuple)
    print(a.list)

