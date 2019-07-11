list1=input()
list1=list(list1)
r=""
for i in range(0,len(list1)-1,2):
  temp=list1[i+1]
  list1[i+1]=list1[i]
  list1[i]=temp
print(r.join(list1))
