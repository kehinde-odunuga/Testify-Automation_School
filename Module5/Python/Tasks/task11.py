
# Module 3b Task 11

# 1. Create a function that accepts two numbers, adds the numbers and prints out the result in the console.
def accept(num1, num2):
    result = num1 + num2
    print('Result: ', result)


# 2. Create a function that return the string value "Testify Python"
def string_value():
    result = 'Testify Python'
    return result

res = string_value()

#Invoke/call the two functions
accept(20, 10)
print(res)