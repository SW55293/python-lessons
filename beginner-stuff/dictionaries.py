colors = {"blue": "Stephanie", "red": "alyssah"}

#return the persons name for given color.. the color is the key
#so you have to give it a color or you'lll get and error
print(colors["blue"])

#check to see if a certaib key value is in the dictionary
#this is asking. Is the key Stephen in the colors dictionary
print('Stephen' in colors)

#another way to get the keys from a dictionary is by printing all the keys
print(colors.keys())
#or
print(list(colors.keys()))

#Listing/Printing all of the values in a dictionary
print(colors.values())
print(list(colors.values()))
#or
values = list(colors.values())
print('The values in colors are: ', values)

#Adding values to an already created dictionary
colors['pink'] = 'Stephen'
print(colors)

#Second way of creating a dictionary
person = dict(name='mom', age=60, height='5.2')
print(person)

###################small program
def favorites(dictionary):
    for key, val in dictionary.items():
        print(f'Hi {key} your favorite food is {val}')

fav_food = {}

while True:
    persons_name = input('Name: ')
    food = input('Favorite Food: ')
    fav_food[persons_name] = food
    
    another = input('Want to add another (y/n): ')
    if another == 'y':
      continue
    else:
      break


favorites(fav_food)


# dictionary = [key | value]

# so when you say dictionary["dog"] = "potato"
# you get
# dictionary = ["dog" | "potato"] 
# and this is dictionary["key"] = "value"