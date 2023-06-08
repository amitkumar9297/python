row=int(input("how many alternating pattern length are you want in a row "))
col=int(input("how many alternating pattern length are you want in a column"))
for x in range(1,col+1):
    if x%2!=0:
        for y in range(row):
            print("* ",end="")
    else:
        for y in range(row):
            print(" *",end="")
    print()
