input='i! love: zoho'
string=list(input)
print(string)
symbol=['!','@','#','$',"%",":"," "]
result=[]

for i in range(len(string)):
        if string[i] not in symbol:
            new=string.pop()
            string.insert(i,new)
        else:
            string.insert(i,string[i])

print(string)
