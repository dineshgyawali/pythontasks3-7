seq = input("Enter a hypen separated set of words: ")
list=[n for n in seq.split('-')]  
list.sort()
print('-'.join(list))