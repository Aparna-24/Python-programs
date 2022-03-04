n=3
r=3
diff=n-r
fact1=1
for i in range(1,n+1):
    fact1=fact1*i

numarator=fact1

fact2=1
for j in range(1,diff+1):
    fact2=fact2*j

denominator=fact2

result=numarator/denominator

print(result)
