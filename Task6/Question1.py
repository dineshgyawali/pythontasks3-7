l1 = ["Apple", "Banana", "cherry", "avocado", "mango"]
l2=[]
for x in l1: 
    for a in x:
        if a.isupper():
            l2.append(x)
        break 

print(l2)


