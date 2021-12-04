class A:
    def __init__(self):
        print(5+8)
class B(A):
    def __init__(self):
        super().__init__()
        print(8-5)
class C(B):
    def __init__(self):
        super().__init__()
        print(5*8)
c=C()