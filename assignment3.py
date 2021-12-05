a=int(input('enter: '))
rev=0
rev
while(a):
    rem=a%10
    rev=rev*10+rem
    a=a//10
r=rev
ans=0
sum=0
while(r):
    rem1=r%10
    ans=ans*10+rem1
    sum+=rem1
    r=r//10
    print(rem1,end="+")
print('=',sum)           