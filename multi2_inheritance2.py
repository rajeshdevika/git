# single level inheritance A->B

class A:
    def __init__(self):
        print("a")


class B(A):
    def __init__(self):
        print("b")
        super().__init__()


obj = B()