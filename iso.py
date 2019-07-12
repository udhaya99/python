n,m=map(str,input().split())
if(len(n)!=len(m)):
  print("no")
else:
  a1=[n.count(i) for i in n]
  a2=[m.count(i) for i in m]
  if(a1==a2):
    print("yes")
  else:
    print("no")
