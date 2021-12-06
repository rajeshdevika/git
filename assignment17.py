a=input('enter: ')
for i in range(0,len(a),2):
    if a[i].isnumeric():
        print(a[i])*a[i+1],end="")
    else:
        print(a[i+1])*a[i],end="")