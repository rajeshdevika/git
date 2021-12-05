a=int(input('enter: '))
num=a
sum=0
rem=0
while(a):
    fact=1
    i=1
    rem=a%10
    while(rem>=i):
       fact*=i
       i+=1
    sum+=fact
    a=a//10
if(num==sum):
    print(num,'is strong')
else:
    print(num,'isnt strong')