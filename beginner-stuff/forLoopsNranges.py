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


################ Ranges
#1 prints 0->9
for x in range(10):
    print(x)

#2 prints 1->3
for x in range(1,4):
    print(x)

#3 prints 0->39 but skips every 2 numbers
for x in range(0, 40, 2):
    print(x)

#4 When you dont know the length of a list & print the list
print()
meatTypes = ['beef', 'pork', 'chicken', 'fish']
for x in range(len(meatTypes)):
    print(x, meatTypes[x])

#2 Print the list backwards
print()
for x in range(len(meatTypes) -1,-1,-1):
    print(meatTypes[x])