from array import *
'''x = array('d', [1,2,3,4,5])
print(len(x))
for element in x:
    print(element)

for i in range(len(x)):
    print(x[i])

p=tuple(x)
print(p)
print(x[1:4])'''

arr=array('d',[1,2,3,4,56,78,98,98.4,99.23])
print("original array",arr)
arr.append(65)
print("modified array",arr)
arr.insert(3,67)
print("insert  67 at index 3",arr)
print("element 56 at index  ",arr.index(56))
print("how many 56 :::::",arr.count(56))
print("original array after modified",arr)
arr.pop()
print("remove a last element from an array",arr)
listt=arr.tolist()
print("convertion array to list",listt)

# BUBBLE SORT METHOD
n=len(arr)
print("length of an  array", n)
flag=False
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            t=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=t
            flag=True
    if flag==False:
        break
    else:
        flag=False
print(" WITH THE HELP OF BUBBLE SORT METHOD****<<<<<<<<<<-------->>>>>>>>>",arr)


# A PROGRAM TO SEARCH POSITION OF ELEMENT >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

enter = float(input("enter a no. to search"))
for i in range(n):
    if arr[i]==enter:
        b=i+1
        break
print("FOUND AT POSITION >>>>>>>>--------------------------->>>>>>>>>>>>>>>>>>>>>>>>",b)

mark=array([[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,5,6,7]])
print(mark)
