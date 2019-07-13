ab=int(input())
ab=list(map(int,input().split()))
ab.sort()
ab.reverse()
if(ab[0]==0):
    print("0")
else:
    for i in ab:
        print(i,end='')
