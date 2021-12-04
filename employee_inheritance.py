class Employee:
    def details(self):
        self.name="Ram"
        self.id=int(input("id:"))
        self.p=20000
        self.status=input("Status(y/n):")
class Pay(Employee):
    def salary(self):
        self.details()
        # super().details()
        if self.id>200 and self.status=='y':
            self.p+=12000
        elif self.id>200 and self.status=='n':
            self.p+=4000
        else:
            self.p+=0
        print(f'Salary:',(self.p))
s=Pay()
s.salary()
