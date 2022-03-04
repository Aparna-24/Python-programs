score=[200,150,160,89,359]
n=3
result=[]
for j in range(n):
    big=score[0]
    for i in range(1,len(score)):

        if score[i]>big:
           big=score[i]
    result.append(big)
    score.remove(big)

print(result)