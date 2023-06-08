n=int(input("enter the number"))
m=n
p=1
a=1
b=n
for i in range(1,n+1):
    for j in range(1,m):
        print(" ",end=" ")
    m=m-1
    for k in range(1,a+1):
        print("*",end=" ")
        print(" ",end=" ")
    a=a+1
    print()
for i in range(1,n):
    for j in range(1,p+1):
        print(" ",end=" ")
    p=p+1
    for k in range(1,b):
        print("*",end=" ")
        print(" ",end=" ")
    b=b-1
    print()

