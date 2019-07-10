num=int(input())
temp=num
rev=0
while(num>0):
  z=num%10
  num=num//10
  rev=rev*10+z
print(rev)
  
