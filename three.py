n=input()
list1=['a','e','i','o','u','A','E','I','O','U']
if(not n.isalnum()):
   print("consonants")
elif(n in list1):
  print("vowels")
else:
  print("invalid")
  

