
name = '     kehinde is my name and kehinde to the world!    '

# len ==> get the size of a string
size = len(name)
print('Size:', size)

# upper ==> convert a string to upper case
upper_value = name.upper()
print('Upper:', upper_value)

# lower ==> convert a string to upper case
lower_value = name.lower()
print('Lower:', lower_value)

# capitalize ==> convert the first character of a string to upper case
capitalized_value = name.capitalize()
print('Capitalized:',capitalized_value)

# count ==> count the occurrence of a value in a string
kehinde_count = name.count('kehinde')
print('kehinde count:', kehinde_count)

e_count = name.count('e')
print('e count:', e_count)

# find ==> count the occurrence of a value in a string
my_position = name.find('my')
print('my position:', my_position)

python_position = name.find('python')
print('python position:', python_position)

# index ==> get the position of a value in a string. If the value is not in string, it throws an exception.
my_index = name.index('my')
print('my index:', my_index)

#python_index = name.index('python')
#print('python index:', python_index)

# strip ==> trim a string, remove excess white space at the beginning and end of a string
stripped_name = name.strip()
print('Stripped:', stripped_name)

# rstrip ==> trim a string, remove excess white space at the end of a string
rstripped_name = name.rstrip()
print('Right-stripped:', rstripped_name)

# rstrip ==> trim a string, remove excess white space at the beginning of a string
lstripped_name = name.lstrip()
print('Left-stripped:', lstripped_name)

# split ==> splits a string to array using the specified value
splitted_name = name.split('and')
print('Splitted (and):', splitted_name)

splitted_name_space = name.split(' ')
print('Splitted (space):', splitted_name_space)

# format ==> format the specified value of a string
# named format
unformatted_one = 'My name is {name}, I am a {occupation}. '
formatted_one1 = unformatted_one.format(name='Kehinde', occupation='Tester')
formatted_one2 = unformatted_one.format(name='Kenny', occupation='QA Engineer')
print('Name formatter 1:', formatted_one1)
print('Name formatter 2:', formatted_one2)

# indexed format
unformatted_index = 'My name is {0}, I am a {1}. I reside in {2}'
formatted_index1 = unformatted_index.format('Kehinde', 'Tester', 'Abuja')
formatted_index2 = unformatted_index.format('Kenny', 'QA Engineer', 'London')
print('Index formatter 1:', formatted_index1)
print('Index formatter 2:', formatted_index2)

# unindexed format
unformatted_index = 'My name is {}, I am a {}. I reside in {}'
unformatted_index1 = unformatted_index.format('Kehinde', 'Tester', 'Abuja')
unformatted_index2 = unformatted_index.format('Kenny', 'QA Engineer', 'London')
print('Unindex formatter 1:', formatted_index1)
print('Unindex formatter 2:', formatted_index2)