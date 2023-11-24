
name = 'Testify'
lesson = 'Python, String, and Concatenation'

# Escape Sequence
article = 'This is an article\nA multiline article\n\tEach text.\b\nA string.'

print(article)

# Raw String
article = r'This is an article\na multiline article\n\tEach text.\b'

print(article)

# Concatenation
group = 'Wood'
attr = 'peckers'
bird = group + attr

print(bird)

print('Python ' + 'Programming' + ' language')

# Arithmetic operators

result = 6 + 4 # addition
print(result)

result = 6 - 4 # subtraction
print(result)

result = 6 * 4 # multiplication
print(result)

result = 6 / 2 # division
print(result)

result = 6 % 2 # modulus
print(result)

print('Compuond Arithmetic operators')

result = 6
result += 4
print(result)

result = 6
result -= 4
print(result)

result = 6
result *= 4
print(result)

result = 6
result /= 2
print(result)

result = 6
result %= 4
print(result)

print('Increment and Decrement')

result = 6
result += 1
print(result)

result = 6
result -= 1

print('Increment and Decrement\n')

print('Lesson 5\n')
print('Conditional Statement')

number = 5
# if statement
if 5 == 5:
    print('5 is equal to 5')

# if-else statement
if 5 == 1:
    print('5 is equal to 5')
else:
    print('5 is not equal to 1')

# elif statement
if 5 == 1:
    print('5 == 1')
elif 5 == 3:
    print('5 == 3')
elif number == 5:
    print('number is 5')

print('Relational Operation\n')

# greater than >
number = 5

if number > 4:
    print('number is greater than 4')

# lesser than <
if number < 6:
    print('number is greater than 6')

# equal to ==
if number == 5:
    print('number is equal to 5')

# not equal to !=
if number != 4:
    print('number is equal to 5')

# greater than or equal to >=
if number >= 3:
    print('number is greater than  or equal to 3')

# lesser than or equal to <=
if number <= 10:
    print('number is lesser than or equal to 10')

# greater than or equal to >=
if number >= 5:
    print('2. Number is greater than  or equal to 5')

# lesser than or equal to <=
if number <= 5:
    print('2. Number is lesser than or equal to 5\n')

print('<== Lesson 6 ==>\n')
print('Logical and\n')

number1 = 10
number2 = 20

if number1 == 10 and number2 == 20:
    print('AND: Number1 = 10, Number2 = 20')

if number1 == 5 and number2 == 20:
    print('AND: Number1 = 5, Number2 = 20\n')

print('\nLogical or\n')

if number1 == 10 or number2 == 20:
    print('OR: Number1 = 10, Number2 = 20')

if number1 == 5 or number2 == 20:
    print('OR: Number1 = 5, Number2 = 20')

print('\nLogical not\n')

if not number1 == 10:
    print('NOT: Number 1 = 10')

if not number1 == 5:
    print('NOT: Number 1 = 5')

# For Loop
print('\nFor loop\n')

fruits = ['Apple', 'Banana', 'Coconut']

for fruit in fruits:
    print('fruit: ', fruit)

name = 'Python'
for ch in name:
    print('Character: ', ch)

# Iterate number
number = 5

for i in range(number):
    print('number: ', i)

# While Loop
print('\nWhile loop\n')

number = 10
while number > 0:
    print('Number is ', number)
    number -= 1


print('\nBreak\n')

number = 5
for i in range(number):
    if i == 3:
        break
    print('For: Number:', i)

while number > 0:
    if number == 3:
        break
    print('While: Number:', number)
    number -= 1

print('\nContinue\n')

number = 5
for i in range(number):
    if i == 3:
        continue
    print('For: Number:', i)

while number > 0:
    if number == 3:
        number -= 1
        continue
    print('While: Number:', number)
    number -= 1

print('\nElse\n')

number = 5
for i in range(number):
    print('For: Number:', i)
else:
    print('for: end of loop')

while number > 0:
    print('While: Number:', number)
    number -= 1
else:
    print('while: end of loop')


print('\nElse and continue\n')

number = 5
for i in range(number):
    if i == 3:
        continue
    print('For: Number:', i)
else:
    print('while: end of loop')

while number > 0:
    if number == 3:
        number -= 1
        continue
    print('While: Number:', number)
    number -= 1
else:
    print('while: end of loop')

print('\nElse and break\n')

number = 5
for i in range(number):
    if i == 3:
        break
    print('For: Number:', i)
else:
    print('while: end of loop')

while number > 0:
    if number == 3:
        break
    print('While: Number:', number)
    number -= 1
else:
    print('while: end of loop')
