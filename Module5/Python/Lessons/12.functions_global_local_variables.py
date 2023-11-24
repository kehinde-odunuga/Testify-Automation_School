
name = 'Kehinde'    # global variable

def greet():
    language = 'Python'     # local variable
    print('Name:', name, 'Language:', language)

def hello():
    framework = 'selenium'     # local variable
    print('Name:', name, 'Framework: ', framework)

platform = 'web'

def print_platform():
    platform = 'Mobile'
    print('Platform:', platform)

print(name)
greet()
hello()
print_platform()