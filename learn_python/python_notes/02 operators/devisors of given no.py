# devisors of a given no.


n = int(input("enter a number"))
l1=[]
for i in range(1,n+1):
    if n%i==0:
        l1.append(i)
print("factor of a no.:",l1)
