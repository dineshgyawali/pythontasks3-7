#Question1
a="1234abcd"
b=a[::-1]
print(b)

#Question2
a="abcSdefPghijQkl"
u=sum(map(str.isupper,a))
v=sum(map(str.islower,a))

print("No. of Upper case characters: ",u)
print("No. of lower case characters: ",v)

