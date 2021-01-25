
from math import sqrt
C=50
H=30
def calculate(D):
    D = int(D)
    a=str(int(sqrt((2*C*D)/H)))
    return a

D= input("Please eneter a few integars separated by comma: ")
D = D.split(",")
D=list(map(calculate,D))
print(",".join(D))