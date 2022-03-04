n=10
arr=[]
for i in range(2,n):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count is 2:
         arr.append(i)

print(arr)
sum=0
for e in arr:
    sum=sum+e

print(sum)


fact=1
for a in range(1,n):
    fact=fact*a
print(fact)