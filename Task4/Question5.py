lines=[]
while True:
    l=input('Enter a line:')
    if l:
        lines.append(l.upper())
    
    for l in lines:
        print(l)
    
    else:
        break; 
