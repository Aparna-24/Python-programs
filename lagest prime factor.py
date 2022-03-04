
number=24
factors=[]
lists=[]
for i in range(2,number+1):
    count=0
    for j in range(1,i+1):
        if i%j == 0:
            count+=1

    if count == 2:
        lists.append(i)

#print(lists);

for e in lists:
    if number%e ==0:
        factors.append(e)

#print(factors)
big=factors[0]

for a in range(1,len(factors)):
    if factors[a]>big:
        big=factors[a]

print(big)


