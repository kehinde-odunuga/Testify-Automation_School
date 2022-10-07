
# Module 3b Task 15

#Declare a list with any value and number of item/element
names = ['Tosan', 'Chioma', 'Michael', 'Chimezie', 'Victoria']

#Print the list in console
print('Names:', names)

#Sort the list
#Print the list in console again
names.sort()
print('Sort:', names)

#Note: you can experiment with the other list functions too in the task.
# Append
names.append('Onene')
print('Append:', names)

# Insert
names.insert(3, 'Chinedu')
print('Insert:', names)

# Len
length = len(names)
print('Length:', length)

# Pop
names.pop(0)
print('Pop:', names)

# Reverse
names.reverse()
print('Reverse:', names)

# Remove
names.remove('Michael')
print('Remove:', names)

# Extend
names.extend(['Sultan', 'Tomiwa', 'Peace', 'Bassey'])
print('Extend:', names)