str1=input("enter a string for calculate the len of string")

print("this is a first method for calculating length of string",len(str1))

i=0
for x in str1:
    i+=1
print("this is a second method for calculating length of string",i)

j=0
while j!=len(str1):
    j+=1
print("this is a third method for calculating length of string",j)

def length_of_string(str2):
    print("this ia a fourth method for calculating length of string",len(str2))

length_of_string(str1)


