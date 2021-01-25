def gen(n):
    print("ist value")
    yield n
    n+=1
    print("2nd value")
    yield n
    n+=1
    print("3rd value")
    yield name

print(next(gen(3)))
