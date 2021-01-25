class Student:
    name="Dinesh"
    __marks=80
    _age=27

    def display(self):
        print(self.name)

class X(Student):
    def __show(self):
        print(self._age)
    def show(self):
        self.__show()

obj1-X()
obj1.show()
obj1.display()
