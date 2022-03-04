from array import array
arr=array('i',[2,4,6,8,9,2])


for i in range(len(arr)):
    sum=0
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            sum+=1
    if sum>0:
        print(arr[i])