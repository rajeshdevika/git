def inp():
    global a,b,c,d
    a=int(input("a:"))
    b=int(input("b:"))
    c=int(input("c:"))
    d=int(input("d:"))
    mul()
    div()
    print(m+v)
def mul():
    global m
    m=a*b
    print(m)
def div():
    global v
    v=c//d
    print(v)
inp()