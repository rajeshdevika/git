a=int(input("enter: "))
if(a>1):
    for i in range(2,a):
        if((a%i)==0):
            print(a,"is not a prime number")
            break
    else:
          print(a,"is prime")
else:
    print(a,"is not prime")