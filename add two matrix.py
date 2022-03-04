x=([
    [1,2,3],
    [3,4,5],
    [6,7,8]
])
y=([
    [2,4,7],
    [4,7,9],
    [1,6,8]
])
result=([
    [0,0,0],
    [0,0,0],
    [0,0,0]
])

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]

for res in result:
    print(res)
