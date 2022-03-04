result=[]
odd=[]
even=[]
list=[]
num=int(input())
for i in range(num):
    x=int(input())
    list.append(x)


for j in list:
    if j%2 != 0:
        odd.append(j)
    else:
        even.append(j)

print(odd+even)




