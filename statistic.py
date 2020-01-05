from math import sqrt


def mean(*args):
    sum = 0
    if type(args[0]) == list or type(args[0]) == tuple:
        print(args)
        print(args[0])
        for data in args[0]:
            sum += data
        print(type(sum / len(args[0])))
        return float(sum / len(args[0]))
    elif not type(args[0]) == list or not type(args[0]) == tuple or not type(args[0]) == dict:
        for data in args:
            sum += data
        return float(sum / len(args))
    else:
        print("Unsupported data type")
        return None


def stddev(*args):
    return sqrt(var(args))


def var(*args):
    sum = 0
    if type(args[0]) == list or type(args[0]) == tuple:
        for data in args[0]:
            sum += float(data) - float(mean(args[0]))
        return sum / len(args)
    elif type(args[0]) != list or type(args[0]) != tuple or type(args[0]) == dict:
        mean = exec("mean(args)")
        for data in args:
            sum += data - mean
        return (sum ** 2) / len(args)
    else:
        print("Unsupported data type")
        return None


if __name__ == "__main__":
    data = [0, 10, 5, 20, -10, 567, 37, -231, 65, 1, 67.724]
    print(type(data))
    print(type(data) == list)
    print(mean(data))
    print(var(data))
    print(stddev(data))
