#lambda functions are anonymous and dont need to be named

def math_func(x, f):
    return f(x)

def cubed(x):
    return x ** 3
#the 2 def functions above will work together to
#calculate the cube of x
#but we can do this in less lines with lambda

lambda x: x ** 3
#returns are implied in lambdas

#or you can also re-use lambdas 
#which shortens it even more
re_use =  lambda x: x ** 3

print(math_func(2, cubed))
print(math_func(2, lambda x: x ** 3))
print(re_use(2))


print('\n------Map Function------------')
# Map Function usually works along side lambdas
# Examples
letters = ['a','b','c','d','e']
#map takes in a function and an iterable like a list/array etc..
#it applies the function to every value of the iterable

# we need to type cast it to a list so we can get a correct print out
type_cast = list(map(str.capitalize, letters))
print(type_cast)

capital_first = list(map(lambda x:x.capitalize() + x, letters))
#ex: print out capitalized then lowercase
#you first add the x.capitalize() then add the x
print(capital_first)

print('\n------Small Programs cubing random ints------------')
from random import randint
# random ints generantes 100 numbers that can be anywhere from
# 1 -> 1000
random_ints = [randint(1,1000) for numbers in range(100)]
print(random_ints)
#cube each 100 number
print(list(map(lambda x: x ** 3, random_ints)))