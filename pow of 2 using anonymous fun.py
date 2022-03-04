terms=10
powers=list(map(lambda x:2**x, range(terms+1)))


for i in range(0,terms+1):

   print("2 power",i,"is",powers[i])