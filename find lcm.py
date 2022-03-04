n1=2
n2=3
if n1>n2:
    max=n1
else:
    max=n2

while(True):
    if max%n1==0 and max%n2==0:
        print("lcm of",n1,"and",n2,"is",max)
        break


    max=max+1








