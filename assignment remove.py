s1={10,20,30,40,50}
s2={30,40,50,60,70}
x=s1.difference(s2)
for i in x:
    s1.remove(i)
print(s1)