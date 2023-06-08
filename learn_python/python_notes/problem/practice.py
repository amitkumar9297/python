'''n=20
m=0
rang=int(input("enter the no. how s first 20 want"))
for i in range(1,rang+1):
    m=m+(n*i)
print(m)'''






'''n=int(input("enter the no."))
for i in range(1,n+1):
    if i%2!=0:
        for i in range(1,n+1):
            print("*",end="")
            print(" ",end="")
    else:
        for i in range(1,n+1):
            print(" ",end="")
            print("*",end="")
    print()'''






'''m=1000
n=2000
a=5
i=1000
j=1005
p=0
while p<=(n-m)/5:
    if i>=1000 and j<2001:
        for k in range(i,j):
            print(k,end="  ")
    i=i+a
    j=j+a
    p=p+1
    print()'''





# code for find out prime no. or not
'''n=50
m=200
a=0
for i in range(n,m+1):
    for j in range(2,n):
        if n%j==0:

            break
    else:
        a=a+n
print(a)'''


'''count=0
for i in range(1000, 2000):
    count=count+1
    print(i,end=' ')
    if count%5==0:
        print("\n")'''




'''import math
n=[2, 4, 8, 16, 32, 64, 128]
for i in n:
    print(math.log(i),"\t", i, "\t", math.log(i**i) , "\t",i**2 , "\t", i**3)'''




n=int(input())
def leap(year):
    leap=False

    if year%4==0 and year%100!=0:
        leap=True
        return leap

    elif year%400==0:
        leap=True
        return leap
    elif year%100==0:
        leap = False
        return leap
print(leap(n))
