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