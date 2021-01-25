from functools import reduce 
list1= [1,2,3,4,5,6,7,8]
result= reduce(list.__add__, (list(x) for x in list1))
 
print(result) 