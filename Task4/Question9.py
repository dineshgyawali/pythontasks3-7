def showNumbers(limit):
    for i in range(0, limit):
        if i==0:
            print(i,end=" ")
            print("EVEN")
        elif i%2==0:
            print(i,end=" ")
            print("EVEN")
        else:
            print(i,end=" ")
            print("ODD")
        

print(showNumbers(4))

