n,m=input().split(' ')
a=0
for i in range(0,len(n)):
  if(n[i]==m[i]):
    a=a+1
if(len(n)==(a+1)):
    print("Yes")
else:
  print("No")
