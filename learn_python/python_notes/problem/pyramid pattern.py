n=int(input("enter the number"))
m=n
a=1
for i in range(1,n+1):
    for j in range(1,m):
        print(" ",end=" ")
    m=m-1
    for k in range(1,a+1):
        print("*",end=" ")
        print(" ",end=" ")
    a=a+1
    print()
