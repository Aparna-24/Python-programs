n=24
m=5
ab1=0
ab2=0
for i in range(n,1,-1):
    ab1=ab1+1
    if i%m is 0:
        result1=i
        break

for j in range(n,n+100):
    ab2=ab2+1
    if j%m is 0:
        result2=j
        break

if ab1<ab2:
    print(result1)
else:
    print(result2)

