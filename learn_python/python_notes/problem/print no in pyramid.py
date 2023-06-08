n=int(input("enter the number"))
m=n
a=1
b=1
c=2
for i in range(1,n+1):
    for j in range(1,m):
        print(" ",end=" ")
    m=m-1
    for k in range(1,a+1):
        c-=1
        print(c,end=" ")
    for l in range(1,b):
        print(l+1,end=" ")
    a=a+1
    b=b+1
    c=a+1
    print()

