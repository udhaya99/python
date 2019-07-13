p = int(input())
q = list(map(int,input().split()))
c = 0
for i in range(p):
    for j in range(i,p):  
        for k in range(j,p):
            if q[i]<q[j]<q1[k]:
                c+=1
print(c) 
