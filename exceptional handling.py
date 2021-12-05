import math
user=int(input("input:"))
b=10
try:
    a=math.factorial(user)
    print(a)
except:
    print("factorial not allowed for neg numbers")
print(b)




"""except Exception as e:
print(e)"""