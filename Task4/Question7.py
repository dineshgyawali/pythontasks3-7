def max_length(y):
     return max(y,key=len)
x=input('enter two string with using space\n')
print(max_length(x.split()))