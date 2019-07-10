num=int(input())
temp=num
rever=0
while(num>0):
  z=num%10
  num=num//10
  rever=rever*10+z
print(rever)
  
