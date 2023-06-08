'''def fun(n):
    f = 1
    for i in range(n, 0, -1):
        f = f*i
    print(f)

fun(5) '''

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


# magic number
a=int(input("enter a number"))
l=[]
for i in str(a):
    l.append(int(i))
print(l)
print(sum(l))
print(sum(l))
