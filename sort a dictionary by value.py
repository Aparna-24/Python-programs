snack={
    'chips':20,
    'chocolate':2,
    'cookies':10,
    'noodles':3,
    'candy':4

}

#as value is first its sorted according to value
ziping=zip(snack.values(),snack.keys())

#print(sorted(ziping))
#print(min(ziping))
print(max(ziping))




#accored to keys
kkeys=zip(snack.keys(),snack.values())
#print(sorted(kkeys))
#print(min(kkeys))
print(max(kkeys))