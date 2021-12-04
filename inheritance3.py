def outer():
    x = 3

    def inner():
        y = 3
        res = x + y
        print("ooooooooooooooooooo")
        return "res"

    print(inner())

    def inner1():
        y = 3
        res = x + y
        return res

    return inner1


a = outer()
print(a())
print(a.__name__)
