
x=0
while x < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Abc123' and username=='Dinesh':
        print('Welcome')
        break
    else:
        print('Please try again.')
        x += 1