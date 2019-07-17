    
aa,bb=list(map(int,input().split()))
ll=list(map(int,input().split()))
for i in range(bb):
  q,s=list(map(int,input().split()))
  print(sum(ll[q-1:s]))
