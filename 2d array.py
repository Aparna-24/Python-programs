
rows=int(input("enter the number of rows:"))
col=int(input("enter the number of column:"))
arr=[]

for i in range(rows):
    l=[]
    for j in range(col):
        item=int(input("enter the number"))
        l.append(item)
    arr.append(l)


print(arr)