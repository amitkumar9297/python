# list: orderd ,mutable ,alllows duplicte elements

'''mylist=["banana","apple","oranges",1,2,3]     # write list in sq bracket
print(mylist,"\n",type(mylist))
item=mylist[1:5]                              # assigned list in another variable
print(item)
for i in mylist:
    print(i)
if "banana" in mylist:                          # check the condition using membership operator
    print("banana is your favourate fruit")
mylist.append("lemon")                          # append is use for add new things in list at last position
mylist.insert(1,"blackberrry")                  # insert is use for insert the things in a list at any position
print(mylist)
a=[1,2,-3,-1,-15,-5,76]
a.sort()                                        # sort is use for sort the list in assending order
print(a)'''


# list: ordered, mutable , allows duplicate element


mylist1=['apple','banana','oranges','mangos']                                                # creating a list
print("the first list","\n \t",mylist1)
mylist2=['lemon','guava']                                                                    # creating a list
print("the second list","\n \t",mylist2)
for i in range(5):
    print()



# concatenation of list or merging the list
mylist3=mylist1+mylist2
print("concatenation or merging the list 1st & 2nd we get a third list","\n \t" ,mylist3)
for i in range(5):
    print()





# copy the list
mylist4=mylist3.copy()
print("copy of the list the 3rd list","\n \t" ,mylist4)
for i in range(5):
    print()






# assigned list means list assigned to new variable ,,,,,,,if we change or update the new list the assigned list also change because these location are same
mylist5=mylist3
print("not a copy list ,it's assigned list ","\n \t",mylist5)
for i in range(5):
    print()






# this is also a copied list
mylist6=sorted(mylist3)
print(" this is also a copied list","\n \t ",mylist3)
for i in range(5):
    print()





# index show the numbering of items in a list
print("position of banana in alist","\n \t ",mylist1.index("banana"))
for i in range(5):
    print()




# copied the 1st list in variable a
a=mylist1.copy()
print("copied list of 1st list","\n \t ",a)
for i in range(5):
    print()




# add a element "blackberry " in list a with the help of insert(index,element) method
# insert help to add an element in a list at specific index
a.insert(1,"blackberry")
print("insert blackberry at index 1 with help of .index fn","\n \t",a)
for i in range(5):
    print()





# copy the second list in variable b
b=mylist2.copy()
print("copied list of 2nd list","\n \t ",b)
for i in range(5):
    print()




# add element in a list with the help of append method
# append is add any element in a list but at last index not specific index
b.append("papaya")
print("add a new item in a list at index last with help of .append fn","\n \t ",b)
for i in range(5):
    print()




# arrange the element of a list in a dictionary order with help of sort() method
# sort method arrange the list in a dictionary order(if elements are string) or ascending order(if elements are digits)
b.sort()
print("arrange the list in assending order oe dictionary order with help of .sort fn","\n \t ",b)
for i in range(5):
    print()




# calculate the length of string and assign length of str b in a new variable c
c=len(b)
print("len of string ","\n \t",c)
for i in range(5):
    print()


# SQUARE OF A NO.
num=list(map(eval ,input("enter a no.").split(" ")))
print(num)
a=list(x*x for x in num )
print(a)




