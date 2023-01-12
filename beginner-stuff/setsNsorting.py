#Sort the numbers using the sort() function
nums = [1,8,4,3,6,5,12,10,45,1]
print(sorted(nums))

#Sorting strings. In python capital letters are prioritized
names = ['Stephanie', 'anna', 'Dog', 'park', 'ant', 'anna']
print(sorted(names))

#Sets do not allow duplicates so they remove them and they dont care about order
print(set(nums))
print(set(names))

#Removing duplicates from a dictionary using set

foods = {'steph': 'chips', 'ben': 'pizza', 'mckay': 'chicken nuggets', 'elijah': 'chips'}
print(set(foods.values()))

#small program to see all the duplicates in a dictionary
def count_colors(dictionary):
    belts = list(dictionary.values())
    #for x in belts: [original code where it didnt remove duplicates lines]
    for x in set(belts):
        num = belts.count(x)
        print(f'there are {num} {x} belts')

user_belt_colors = {}

while True:
    user_name = input('Enter your name: ')
    user_color = input('Enter a belt color: ')
    user_belt_colors[user_name] = user_color

    add_another = input('Want to add more users and there colors? (y/n): ')
    if add_another == 'y':
        continue
    else:
        break

count_colors(user_belt_colors)