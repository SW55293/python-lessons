#Function example
def greet():
    print("Stephanie")

greet()

#Passing data into a function
def greetings(name, time):
    print(f'Good Morning {name} it is {time}')

greetings('Stephanie', '2:00')

#Asking user for input
def askUser(name, color):
    print(f'Hi {name} your favorite color is {color}')

fname = input('Enter your name: ')
fcolor = input('Enter your favorite color: ')

askUser(fname, fcolor)

#Defining area of a circle
r = input('Enter a radius: ')
l = input('Enter a length: ')

def area(radius):
    #print(3.142*radius*radius)
    return 3.142*radius*radius

#Use the area without printing it to calculate volume in another function
def volume(area, length):
    print('The volume is: ', area*length)

#store the return or def area() in a variable
calculated_area = area(r)

#2 ways you can do the below
volume(calculated_area, l)
volume(area(r),l)