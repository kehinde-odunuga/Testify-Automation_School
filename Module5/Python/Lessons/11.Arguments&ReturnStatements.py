
print('Parameters')

# required parameter
print('\n==>required parameter')

def greet(name):
    print('Hello, ', name)

greet('Kehinde')

# default parameter
print('\n==>default parameter')

def add(num1=10, num2=15):
    result = num1 + num2
    print('Result: ', result)

add()
add(5)
add(5, 5)

# keyword argument
print('\n==>keyword argument')

def minus(num1, num2):
    result = num1 - num2
    print('Result: ', result)

minus(num1=10, num2=5)
minus(num2=5, num1=10)

# arbitrary/variadic argument
print('\n==>arbitrary/variadic argument')

def print_value(*args):
    print('Argument: ', args, args[0])

#printValue()
print_value(1)
print_value(1, 2)
print_value(1, 2, 3)

# arbitrary/variadic keyword argument
print('\n==>arbitrary/variadic keyword argument')

def print_kvalue(**kargs):
    print('Argument: ', kargs, kargs['num1'], kargs['num2'])

print_kvalue(num1=1, num2=2)

# return statement
print('\n==>return statement')

def add_and_return(num1, num2):
    result = num1 + num2
    return result

res = add_and_return(50, 50)
print('50 + 50: ', res)

def check_number(number):
    if number > 5:
        return
    print('Number: ', number)

check_number(1)
check_number(3)
check_number(5)
check_number(6)
check_number(10)