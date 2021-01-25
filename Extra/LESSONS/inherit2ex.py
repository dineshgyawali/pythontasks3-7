class Animal:
    def __init__(self,name):
        self.name=name

    def show(self):
        print("Name of the animal is: ",self.name)

class pets(Animal):
    def __init__(self,name,type):
        Animal.__init__(self,name)
        self.type-type

    def food(self):
        print("the pet food is available in supermarket")

a1=Pets("Tommy","Dog")
a1.show()
a1.food()