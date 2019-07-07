n,m=map(int,input().split( ))
for i in range(n,m+1):
  sum=0
  temp=i
  while(temp>0):
    d=i%10
    sum=sum+(d*d*d)
    i=i//10
 if(i==sum):
  print(i,end=" ")
 
