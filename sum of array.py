from array import *

arr1=array('i',[])

length=int(input("enter the length:"))
for i in range(length):
    x=int(input("enter the number:"))
    arr1.append(x)
    
print(arr1)
sum=0
for e in range(length):
    sum+=arr1[e]

print("the sum of the given array is ",sum)
