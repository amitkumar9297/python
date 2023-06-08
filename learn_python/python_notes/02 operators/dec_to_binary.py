dec = int(input("enter decimal no. to convert in binary form"))
tem=""
while dec>=1:
    rem=str(dec%2)
    dec=dec//2
    tem=tem+rem
print(len(tem))
b=""


for re in tem:
    b=re+b
print(b)


