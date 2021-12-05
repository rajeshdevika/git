n = "ocean"
a = 5
for i in range(a):
    for j in range(a):
        if (i == j):
            print(n[i], end=" ")
        elif (i + j == 4):
            print(n[j], end=" ")
        else:
            print(' ', end=" ")
    print()

'''for i in range(5):
    print(i*' ',n[i],' '*(i+l),n[i])
    l-=2