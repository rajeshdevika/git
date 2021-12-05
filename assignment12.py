a=[[1,["ocean","pondy","2"]],[2,["xxx","yyy","22"]]]
d={}
for i in a:
    d[i[0]]=i[1]
print(d)
i=int(input(" "))
for item in d:
    if(i==item):
        x=d.get(item)
        for y in range(len(x)):
            if(y==0):
                print("name :",x[y])
            if(y==1):
                print("place :",x[y])
            if(y==2):
                print("age :",x[y])

