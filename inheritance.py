class Demo:
    age=12
    def display(self,name,address):
        self.name=name
        self.address=address
p1=Demo()
p1.display("ocean","pondy")
p2=Demo()
p2.display("academy","chennai")
print(p1.name)
print(p2.age)