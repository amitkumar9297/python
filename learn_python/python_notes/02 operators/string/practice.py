'''for z in str2:
                str3=str2+str3
        #print(str2)
            if str2==str3:
                print("palindrome")'''

size = 256
def solve(s) :
   freq = [0] * size
   print(freq)
   for i in range( 0, len(s)) :
      freq[ord(s[i])] = freq[ord(s[i])] + 1
   odd_count = 0
   for i in range(0, size) :
      if freq[i] % 2 == 1 :
         odd_count = odd_count + 1
      if odd_count > 1:
         return False
   return True
s = "aarcrce"
print(solve(s))


