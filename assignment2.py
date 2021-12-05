a=int(input("enter: "))
sum=0
for i in range(1,a):
    if(a%i==0):
        print(i)
        sum+=i
if(sum==a):
    print(a,'is perf')
else:
    print(a,'isnt perf')