num=int(input("enter a number for checking prime or not"))
for x in range(2,num):
    if num%x==0:
        break
else:
    print(r"this is a prime numbe",num)
