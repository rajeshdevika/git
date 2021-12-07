class Father:
    def __init__(self,job):
        self.occupation=job
        print("father work as:",self.occupation)
class Mother:
    def __init__(self,job):
        self.work_as=job
        print("mother work as",self.work_as)
class Child(False,Mother):
        def __init__(self,age,birth_month):
            self.age=age
            self.birth_month=birth_month
            print("childs age",age)
            print("chils month"birth_month)

young=child()
