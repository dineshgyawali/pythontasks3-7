class Birds:
    def __init__(self,type):
        self.type=type

    def show(self):
        print("Bird type: ",self.type)

    def display(self,color):
        self.color=color
        return self.color

class Snakes:
    def __init__(self,name):
        self.name=name

    def show(self):
        self.type="poisonous"
        print("Snake type: ",self.type)

    def display(self,size):
        self.size=size
        return self.size

obj1=Birds("Parrot")
obj2=Snakes("Cobra")
obj1.show()
obj2.show()
print(obj1.display("Green"))
print(obj2.display("long"))
