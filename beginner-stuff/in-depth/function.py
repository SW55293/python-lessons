# Functions dont always need to include parameters
# Function may or may not have a return value
# You can have multiple return objects. ex: return list1, list2


def input_from_user():
    return input('-> ')


print('What is your name?')
name = input_from_user()

print('What day is it today?')
day = input_from_user()

print('What is your favorite bird?')
bird = input_from_user()

print(f'Your inputs are: {name}, day is {day}, favorite bird is {bird}')