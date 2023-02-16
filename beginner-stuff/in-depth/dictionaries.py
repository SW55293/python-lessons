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