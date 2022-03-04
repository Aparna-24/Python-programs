def swap(a1, b1):
     temp=a1
     a1=b1
     b1=temp
     print("the value of a is now ", a1)
     print("the value of b is now ", b1)

a = int(input("enter the value for a:"))
b = int(input("enter the value for b:"))
swap(a,b)