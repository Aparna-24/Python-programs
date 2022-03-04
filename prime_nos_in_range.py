start = 20
stop = 30

for i in range(start, stop):
    count = 0
    for j in range(1, i+1):
        if i%j is 0:
          count = count+1
    if count is 2:
      print(i)

