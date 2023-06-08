# tuple: ordered,immutable, allow duplicate element
tup=(1,2,3)
print(type(tup))

# CONVERT TUPLE TO LIST
tup1=('a','p','p','l','e')
print(tup1,end=" \t \t")
mylist=list(tup1)
print(mylist)
print("*****************************************************************************************************************")
# CONVERT LIST TO TUPLE
mylist1=['m','a','n','g','o']
tup2=tuple(mylist1)
print(mylist1,end="\t \t")
print(tup2)
print("*****************************************************************************************************************")
# INDEX OR SLICING THE TUPLE
a=(1,2,3,4,5,6,7,8,9,0)
b=a[2:9:2]
c=a[::-1]
print(b)
print(c)
print("*****************************************************************************************************************")

# ASSIGNED TUPLE TO MULTIPLE VARIABLES

bio=('jansy',24, 'usa')
name,age,country=bio
print(name,age,country)
print("*****************************************************************************************************************")


# ASSIGNED TUPLE ELEMENTS TO MULTIPLE VARIABLE

digit=(1,2,3,4,5,6,7,8,9)
i1,*i2,i3=digit
print('i1',i1)
print("i2",i2)
print("i3",i3)
print("*****************************************************************************************************************")


# CALCULATE THE SIZE OF LIST AND TUPLE
import sys
tupl=(0,1,2,"hello",True)
listt=[0,1,2,"hello",True]
print(sys.getsizeof(tupl),"bytes")
print(sys.getsizeof(listt),"bytes")
print("*****************************************************************************************************************")


# MEASURE THE RUNNING TIME WHEN RUN X TIMES

import timeit
print(timeit.timeit(stmt="(1,2,3,4,5)",number=1000000))
print(timeit.timeit(stmt="[1,2,3,4,5]",number=1000000))


dd=[int(x) for x in input().split(" ")]
