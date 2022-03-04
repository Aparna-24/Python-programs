n=153
sum=0
temp = n
while n!=0:
    r = n%10
    sum = sum+(r*r*r)
    n//=10
n = temp
if n is sum:
    print(n, " is an amstrong number")
else:
    print(n, " is not an amstrong number")


