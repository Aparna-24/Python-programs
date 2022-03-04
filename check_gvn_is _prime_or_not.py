n = 7
counter = 0
for i in range(1, n+1):
    if n % i == 0:
        counter = counter+1


if counter is 2:
    print(n, " is prime")
else:
    print(n, " is not prime")

