n=[2,3,4,5,4,3,5,4,9,8]
str1="".join(map(str,n[-1:-5:-1]))
print(str1)
str2="".join(map(str,n[-5:-8:-1]))
print(str2)
str3="".join(map(str,n[0:3:1]))
print(str3)
k=("("+str3+")"+"  "+str2+"-"+str1)
print(k)