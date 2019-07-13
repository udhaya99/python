a=int(input())
b=list(map(int,input().split()))
so=0
but=[]
for i in range(0,a+1):
    if(b.count(i)>1):
      but.append(i)
if(len(but)==0):
    print("unique")
e=sorted(but)
print(' '.join(map(str,e)))
