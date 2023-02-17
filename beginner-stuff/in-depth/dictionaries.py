# There are 3 types of ways to write a dictionary

first = {'name': 'steph', 'class': 'math'}

second = {
    'steph': '81836958',
    'elijah': '2364233',
}

third = {
    'a':
    {
        'apple': 'computer/tech company',
        'google': 'tech company'
    },
    'b':
    {
        'color': 'black',
        'colors': 'red,blue,green,red'
    }
}

# print parts of the third dcitionary
print(third['a'])
print(third['b'])

#printing even more specific portions of a dict if you know what it contains
#so say you want the info at the key a, google. you can print that
print(third['a']['google'])

# Printing out items in dictionaries
# just the keys
for keys in first:
    print(keys)
for keys in second:
    print(keys)
for keys in third:
    print(keys)

#printing out keys and values
for items in first.items():
    print(items)
for items in second.items():
    print(items)
for items in third.items():
    print(items)


# unpacking tuples
for item in first.items():
    key, value = item
    print(f'key = {key} | value = {value}')
print('--------------------------')
for key, value in second.items():
    print(f'key = {key} | value = {value}')