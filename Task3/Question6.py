var=list(range(1,31))
x=var[0:5]
y=var[25:]
x.extend(y)

z=map(lambda a:a**2,x)
print(list(z))