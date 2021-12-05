a=int(input("enter: "))
count=0
for i in range(1,a+1):
    if(a%i==0):
        count+=1
if(count>2):
    print(a,'not prime')
else:
    print(a,'prime')