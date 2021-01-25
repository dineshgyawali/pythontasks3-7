class Vehicles:
    def __init__(self,name):
        self.name=name

    def display(self):
        print("this is the name of the vehicle:{}".format(self.name))
class Cars(Vehicles):
    pass

b1=Cars("Acura")
b1.display()