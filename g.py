p1,r2=map(int,input().split())
z3=[]
x4=0
for i in range(p1):
    z3.append(list(map(int,input().split())))   
for i in range(p1):
    for j in range(r2-1):
        for k in range(j+1,r2+1):
            if z3[i][j:k]==[1]*len(z3[i][j:k]):
                 if all(z3[p1+i][j:k]==[1]*len(z3[p1+i][j:k]) for p1 in range(len(z3[i][j:k])-1)):
                     if len(z3[i][j:k])>x4:
                        x4=len(z3[i][j:k])
if len(z3)==1 and len(z3[0])==1 and z3[0][0]==1:
    print(1)
for i in range(x4):
    print(*[1]*x4) 
