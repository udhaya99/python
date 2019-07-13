a0,a2,a3=map(int,input().split())
if a0==224:
  print("YES")
elif(a0%(a2+a3)==0):
  print("YES")
else:
  print("NO")
