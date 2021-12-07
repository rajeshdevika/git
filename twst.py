class Demo:
    def summ(self,a=None,b=None,c=None):
        self.a,self.b,self.c=a,b,c
        if (self.a!=None and self.b!=None and c!=None):
             self. result = a+b+c
        elif(a!=None and b!=None ):
           self. result =a+b
        elif(a!=None ):
            self.result = a
        print(self.result)
obj1=Demo()
obj1.summ(4,5)