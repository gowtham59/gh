ni1,mi2=map(int,input().split())
tem=[]
x3=0
for i in range(ni1):
    tem.append(list(map(int,input().split())))   
for i in range(ni1):
    for j in range(mi2-1):
        for k in range(j+1,mi2+1):
            if tem[i][j:k]==[1]*len(tem[i][j:k]):
                 if all(tem[p+i][j:k]==[1]*len(tem[p+i][j:k]) for p in range(len(tem[i][j:k])-1)):
                     if len(tem[i][j:k])>x:
                        x=len(tem[i][j:k])
if len(tem)==1 and len(tem[0])==1 and tem[0][0]==1:
    print(1)
for i in range(x3):
    print(*[1]*x3) 
