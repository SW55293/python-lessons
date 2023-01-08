#add the int() method to save as an in : type casting
age = int(input('enter your age: '))

if age < 10:
    #code block needs to be indented
    print('you are: ', age, 'years old')
elif age > 10:
    print('you are old')
    #you can add as many elif as youd like...no limit!!
else:
    print('i dont know how old you are')

#another small program
meat = input('do you eat meat? (y/n): ')

if meat == 'y':
    print('Meat Menu')
else:
    print('Veg Menu')

############ While Loops
score = 100
num = 0 
while num < score:
    print(num)
    num += 1

# Print only even
while num < score:
    if num % 2 == 0:
        print(num)
    num += 1