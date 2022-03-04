from array import array

arr=array('i',[11,15,6,8,9,10])
sum=16

for i in arr:
    for j in arr:
        result=i+j

        if result == sum:
            print(i,j)
            break
