# cycle through list and print out using fo loop
names = ['steph', 'cat', 'dog', 'water']

for x in names:
    print(x)

#cycle through and only print some
letters = ['a', 'b', 'c', 'd', 'e', 'f']

for x in letters[0:3]:
    print(x)

#another example
colors = ['blue', 'red', 'yellow']

for x in colors:
    if x == 'black':
        print(f'{x} not in the list')
        #add a break if you dont want it to continue
        break
    else:
        print(x)