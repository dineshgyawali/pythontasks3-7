#using for loop make a list which creates squares from 1 to 10. 
x=[]
for i in range(1,11):
    x.append(i*i)
print(x)


#using list comprehension
x=[x**2 for x in range(1,11)]
print(x)


#hence using just 1 line, we got the same result. 

# Exercise: to select only the even numbers
x=[x for x in range(1,101) if x%2==0]
print(x)


#Exercise: to select only the numbers divisible by 3 and 5
x=[x for x in range(1,101) if x%3==0 and x%5==0]
print(x)


#same command with string variable
#print only those letters which are consonants
x=[char for char in "consultadd" if char not in]