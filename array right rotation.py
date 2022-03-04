array=[10,20,30,40,50]
n=2

length=len(array)
for e in range(n):
    temp = array[0]
    
    for i in range(0,length-1):
        array[i]=array[i+1]

    array[length-1]=temp

print(array)
