l1=[]
for i in range(1,21):
    l1.append(i)
var=filter(lambda x:x%2==0,l1)
print(list(var))