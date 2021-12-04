global s,m,h,d,n,y
def time(q):
    s=q%60
    x=q//60
    d=0
    h=0
    n=0
    y=0
    if x>59:
        a=x
        h=x//60
        x=a%60
    if h>23:
        b=h
        d=h//24
        h=b%24
    if d>29:
        e=d
        n=d//30
        d=e%30
    if n>11:
        v=n
        y=n//12
        n=v%12
    return("Y:",y,"M:",n,"D:",d,"H:",h,"M:",x,"S:",s)
print(time(864001))