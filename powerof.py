n,m=map(int,input().split())
flag=1
for i in range(1,100):
  if(pow(m,i)==n):
      print("yes")
      flag=0
      break
if(flag==1):
  print("no")
