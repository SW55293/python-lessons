
# String Formatting so that we can ask for input and output it in less steps
num = 55.36
num2 = 555.999

#Previous way
print("first number", num, "second number", num2)

#Format method
#you use the .format() then give the variables and add the curly braces to your string and place the index inside
print('number one: {0} and number 2 is: {1}'.format(num,num2))

#only output a certain number of numbers after decimal
print('number one: {0:.2f} and number 2 is: {1:.2f}'.format(num,num2))


#using f-strings
print('Second way')
print(f'number 1 = {num} and number 2 = {num2}')

#format it
print(f'number 1 = {num:.4f} and number 2 = {num2:.4f}')