class Even:
    def even(self,length):
         for  i in range(length- 1):
             if(i%2==0):
               print(i)
               print()
class Odd:
      def odd(self,length):
         for i in range(length-1):
             if(i%2!=0):
                 print(i)
                 print()

class Work(Even,Odd):
        def odd_even(self,len):
             self.len=len
             if(len%2==0):
                 return  self.even(len)
             else:
                 return  self. odd(len)
obj1=Work()
n=int(input("entre the number"))
obj1.odd_even(n)


