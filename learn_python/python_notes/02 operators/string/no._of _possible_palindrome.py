str1=list(input("enter a string to find the number of possible palindrome string"))
global str2
global str3

for x in range(len(str1)):

    #print(x)
    for y in range(len(str1)):
        str3=[]
        #print(y)
        if x!=y:
            str1[x],str1[y]=str1[y],str1[x]
            str2=str1
            print(id(str1))
            print(str2)
            str2.reverse()
            for z in str2:
                str3.append(z)

            if str3==str2:
                print("palindrome")





