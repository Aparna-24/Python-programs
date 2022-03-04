min=150
max=1600

for n in range(min, max):
    temp = n
    order=len(str(n))
    sum = 0
    while temp>0:
        r = temp%10
        sum+=r**order
        temp//=10

    if n == sum:
        print(n, "is an amstrong number")
