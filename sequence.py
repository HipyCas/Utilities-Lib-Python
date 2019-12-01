class Sequence:
    def __init__(self, *args):
        self.terms = args
        if args[1] - args[0] == args[2] - args[1] and args[3] - args[2] == args[2] - args[1] and args[3] - args[2] == args[1] - args[0]:
            self.type = 0   # 0 == Arimetica
            self.difference = args[1] - args[0]
            self.generalterm = str(args[0] - self.difference) + " + " + str(self.difference) + " * n"
            self.recursive = "tn-1 + " + str(self.difference)
        elif args[1] / args[0] == args[2] / args[1] and args[3] / args[2] == args[2] / args[1] and args[3] / args[2] == args[1] / args[0]:
            self.type = 1   # 1 == Geometrica
            self.difference = args[1] / args[0]
            self.generalterm = str(args[0]) + " * (" + str(self.difference) + " ** (n-1))"
            self.recursive = "self.terms[n-1] * " + str(self.difference)
        else:
            self.type = -1

    def term(self, n):
        print(self.generalterm.replace("n", str(n)))
        exec("self.term = " + self.generalterm.replace("n", str(n)))
        print(self.term)
        return self.term


if __name__ == "__main__":
    a = Sequence(1,3,5,7,9)
    print(a.terms)
    print(a.type)
    print(a.difference)
    print(a.generalterm)
    print(a.recursive)
    print(a.term(10))
    print("-----")
    g = Sequence(int(input("t1:")),int(input("t2:")),int(input("t3:")),int(input("t4:")))
    print(g.terms)
    print(g.type)
    try:
        print(g.difference)
        print(g.generalterm)
        print(g.recursive)
        print(g.term(10))
    except AttributeError:
        print("Is that really a sequence?")
