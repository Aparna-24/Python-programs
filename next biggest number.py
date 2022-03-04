from array import array
num=array('i',[8,1,4,6,9,5])


for i in num:
    print('\n')
    print(i,'->' ,end="")
    for j in range(1,100):
        sum=i+j
        if sum in num:
            if i<sum:
             print(sum)

             break



