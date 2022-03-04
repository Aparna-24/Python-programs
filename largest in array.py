from array import *

arr=array('i',[])

length=int(input("enter the length of array:"))
for i in range(length):
    x=int(input("enter the number:"))
    arr.append(x)

print(arr)

big=arr[0]
for a in range(1,length):
     if arr[a]>big:
         big=arr[a]

print("the biggest value is",big)