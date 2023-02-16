# Tuples are like lists but you cannot change them once created
# ypu use parenthesis and not square brackets

names_age = ('steph', 20, 'elijah', 10, 78, 90, 'dogs are cool')
another_tuple = ('parenthesis', 'mixure of different types')

# print a random index
print(names_age[3])

# print out the methods
print(dir(names_age))

print(names_age.index('steph'))

# you look for random values that may be inside your tuple
# you get a boolean in return
print('dog' in names_age)