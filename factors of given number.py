number=int(input("enter the number:"))
print("the factors of ",number,"is")
for i in range(1,number+1):
    if number%i == 0:
        print(i)
