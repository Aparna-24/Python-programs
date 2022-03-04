x=([
    [5,6],
    [3,5],
    [8,1]
])
res=([
    [0,0,0],
    [0,0,0]
])
for i in range(len(x[0])):
    for j in range(len(x)):
        res[i][j]=x[j][i]

for r in res:
    print(r)