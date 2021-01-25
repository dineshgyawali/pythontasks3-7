from abc import ABC,abstractmethod
class X(ABC):

    @abstractmethod
    def do(self):
        pass

    def show(self):
        pass

class Y(X):
    def do(self):
        print("this is the do method")

    def show(self):
        print("this is show method")

b=Y()
b.do()