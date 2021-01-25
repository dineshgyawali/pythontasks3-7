def f1(func):
    print("f1 started")
    func()
    print("f1 ended")

def f2():
    print("hello")

f1(f2)

#Example 2

def f1(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper

@f1
def f2():
    print("f2")

f2()


#Example 3
import time
def timer(func):
    def func2():
        start-time.time()
        func()
        print("Function took:",time.time()=start,"seconds")
    return func2

@timer
def run():
    time.sleep(2)

add()