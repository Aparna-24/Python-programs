numbers=[2,5,7,1,9,14]
big=numbers[0]

for i in range(1,len(numbers)):
    if numbers[i]>big:
        big=numbers[i]
#print(i,big)
numbers.pop(i)

sec_large=numbers[0]
for j in range(1,len(numbers)):
    if numbers[j]>sec_large:
        sec_large=numbers[j]

print(sec_large," is the second largest number.")