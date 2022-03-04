array=[20,30,40,50]
n=2
length=len(array)

for j in range(1,n+1):
    temp=array[length-1]

    for i in range(length-1,0,-1):
        array[i]=array[i-1]
    array[0]=temp

print(array)