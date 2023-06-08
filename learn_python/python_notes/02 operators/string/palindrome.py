str1=input("enter a string to check palindrome or not")
reverse=""
for x in str1:
    reverse=x+reverse

if str1==reverse:
    print(" this ia a palindrome string")
else:
    print(" this is not a palindrome string")

