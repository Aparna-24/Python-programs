n=56
sum=0
for i in str(n):
    sum=sum+int(i)

value=str(sum)
rev_value=reversed(value)

if list(value)==list(rev_value):
    print("its a palinrome")
else:
    print("not a palindrome")