n=int(input())
val=input().split()
a=[]
for i in sorted(val):
  a.append(i)
if(a==val):
  print("yes")
else:
  print("no")
