
print('\nFunctions\n')

def greet():
    print('Hello world')

def accept(cb):
    cb('Hello')

hello = lambda:print('Hello world Anonymously')
hello()
accept(lambda x: print(x))