from random import randint


rates = {
    "CAD": {
        "EUR": 0.68,
        "usd": 0.75,
        "jpy": 82.92,
        "chf": 0.75
    },
    "EUR": {
        "CAD": 1.44
    }
}


class Bank:
    """

    """

    def __init__(self, name, initials, location, number):
        self.name = name
        self.initials = initials.upper()
        self.location = location
        self.number = number
        self.identifier = str(location) + str(number)


class Account:

    def __init__(self, bankid, quantity, currency, number):
        self.bank = bankid
        self.currency = currency
        self.balance = quantity
        self.number = number

    def setSecurity(self, pin):
        self.pin = pin

    def get(self, currency="EUR"):
        try:
            return self.balance * rates[self.currency][currency]
        except KeyError:
            if self.currency == currency:
                return self.balance
            else:
                return "Currency doesn't exist"

    def simpleinterest(self, rate, time):
        return self.balance * rate * time

    def compoundinterest(self, rate, time):
        return self.balance * (rate ** time) - self.balance


class NextCurrency:

    identifiers = []

    def __init__(self, name, initials, **kwargs):
        self.name = name
        self.initials = initials
        print("Identifier")
        self.identifier = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
        print(self.identifier)
        while self.identifier in self.identifiers:
            self.identifier = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
            print(self.identifier)
        self.identifiers.append(self.identifier)
        print("Mean")
        mean = 0
        print(mean)
        for rate in kwargs.values():
            mean += rate
            print(mean)
        mean /= len(kwargs)
        print(mean)
        print("---")
        if mean == 1:
            self.rates = kwargs.copy()
        else:
            print("Invalid rates")
            raise ValueError
        print(kwargs)
        this = {}
        others = {}
        for exchange in kwargs.items():
            print("Starting ")
            print(exchange)
            this[exchange[0]] = "*" + str(exchange[1])
            print("step 1 done")
            try:
                others[exchange[0]] = (exchange[0], {exchange[0]: exchange[1]})
                print("This worked")
            except ZeroDivisionError:
                print("Value 0")
                others[exchange[0]] = (exchange[0], 0.00)
            print("step 2 done")
        print("...")
        print("Others exchange dict")
        print(others)
        print("...")
        print("Adding this currency")
        rates[self.initials] = this
        print("...")
        for other in kwargs.items():
            print("Applying ")
            print(other)
            if other[0] in rates:
                print("Existe. Aplicando")
                rates[other[0]][self.initials] = "/" + str(other[1])
            else:
                print("No existe. Creando y aplicando")
                rates[other[0]] = {self.initials: "/" + str(other[1])}
            print(rates[other[0]])
            print(rates[other[0]]["PP"])
            print()
            print("applied")
        print("Rates")
        print(self.rates)
        print("Identifier")
        print(self.identifier)


if __name__ == "__main__":
    nextBank = Bank("next>>Bank", "NEXT", "WW", 00)
    print("acc")
    acc = Account(nextBank.identifier, 500, "CAD", 534)
    print(rates["CAD"]["EUR"])
    print(acc.get("CAD"))
    print("ac")
    ac = Account(nextBank.identifier, 500, "EUR", 345)
    print(ac.get("EUR"))
    print(ac.get("CAD"))
    print("nc")
    nc = NextCurrency("Pepe", "PP", EUR=2, USD=0.00000000000)
    print(NextCurrency.identifiers)
    print("rates")
    print(rates)
