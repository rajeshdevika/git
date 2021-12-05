a=input('enter: ')
count=0
c=input('enter: ').strip()
for i in range(len(a)):
    if(c==a[i]):
        count+=1
print(count)