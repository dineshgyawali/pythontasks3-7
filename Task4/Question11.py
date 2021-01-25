l1=[1,2,3,4,5,6,7,8,9,10]
l2 = map(lambda x: x**2, filter(lambda x: x%2==0, l1))
print(list(l2))