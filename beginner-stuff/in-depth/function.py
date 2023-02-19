# Functions dont always need to include parameters
# Function may or may not have a return value
# You can have multiple return objects. ex: return list1, list2

# When passing in mutable data types such as lists, array, dictionaries ..
# to other functions, the calling functions only have the refernece to the place
# where that data is stored, they dont duplicate that data or make a copy
# for themselves. they change the original data



def input_from_user():
    return input('-> ')


print('What is your name?')
name = input_from_user()

print('What day is it today?')
day = input_from_user()

print('What is your favorite bird?')
bird = input_from_user()

print(f'Your inputs are: {name}, day is {day}, favorite bird is {bird}')