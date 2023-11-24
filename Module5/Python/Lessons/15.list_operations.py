
languages = ['python', 'java', 'c#', 'java']
print('List:', languages)

# append ==> add new item at the end of list
languages.append('javascript')
print('Append:', languages)

# insert ==> add new item at any position in the list
languages.insert(0, 'c')
languages.insert(2, 'php')
print('Insert:', languages)

# pop ==> remove item from specified position in the list
languages.pop(0)
languages.pop()
print('Pop:', languages)

# remove ==> remove item by value
languages.remove('php')
print('Remove:', languages)

# count ==> return the number of occurence from a list
count_java = languages.count('java')
print('List:', languages)
print('Count Java:', count_java)

# len ==> count the number of items in a list
length = len(languages)
print('Length:', length)

# clear ==> deletes all items in a list
languages.clear()
length = len(languages)
print('Clear:', languages, length)

languages = ['python', 'java', 'c#']

# copy ==> return a copy of the list
languages_copy = languages.copy()
print('Copy:', languages_copy)

# reverse ==> reverse the order of items in a list
before_reverse = languages.copy()
languages.reverse()
print('Before everse:', before_reverse, ', after_reverse:', languages)

languages = ['python', 'java', 'c#', 'c', 'smalltalk', 'ruby']

# sort ==> sort item in the list by either ascending or descending order
languages.sort()
print('Sort-asc:', languages)
languages.sort(reverse=True)
print('Sort-des:', languages)

# extend ==> add the content of a specified list to the current list
languages.extend(['visual basic','brainfuck', 'ring', 'sql', 'powershell'])
print('Extend:', languages)