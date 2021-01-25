#To create a new list with the fruits containing alphabet 'o' from the list of fruits

l1=["mango", "apple", "orange","avocado"]
newlist = []
for x in l1:
    if "o" in x:
        newlist.append(x)
print(newlist)


