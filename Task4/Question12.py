def func():
    return 5/0

try:
    func()
except ZeroDivisionError:
    print("divided by zero!")
except:
    print('exception')