def fact(n):
    if n is 0:
        return 1
    else:
        return n*fact(n-1)

num = 9
if num < 0:
    print("sorry no factorial for this number")
elif num is 0:
    print("factorial for this number is", 1)
else:
    print("factorial of this number is", fact(num))

#using for loop
m=9
facto=1
for i in range(1,m+1):
    facto=facto*i
print(facto)