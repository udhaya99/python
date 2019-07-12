a,b=map(int,input().split())
c=0
for i in range(a,b+1):
  d=0
  for j in range(2,i):
    if(i%j==0):
      d=1
      break
  if(d==0):
    c=c+1
print(c)
