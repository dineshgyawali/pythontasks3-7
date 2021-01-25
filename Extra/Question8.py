l1=[2,4,6,8,12]
l2=[1,3,5,7,9,13]

for i in range (0,5):
    x=int(input("Enter a number 0 to 51: "))
    if x%2==0:
        y=int(input())
        l1.append(y)
    print(l1)
    
    if x%2!=0:
        y=int(int(input()))
        l2.append(y)
    print(l2)