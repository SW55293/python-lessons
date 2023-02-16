# A more in-depth look into list Method and functions that are built in
# and the id's and memory
'''
Methods vs Functions

Methods are usually of the .method()
example: object.method()

While Functions dont need a dot/period. so function()
example: function(object)
'''

numbers = [15,6,12,5,36,10,1,8,9,10,1,1]
classes = ['Comp Sci', 'physics', 'math', 'p.e']

print('UN-Sorted list of Numbers =', numbers)
print('Classes = ', classes)

# sorted() Function
print(sorted(numbers))

#before i use the .sort.. Testing purposes
print('before .sort() method = ', id(numbers))
# using the .sort() Method | Cant have it inside print function. wont work. Sorts in-place
numbers.sort()  
print(numbers)

# To take a look at the memory positions and see that .sort() does in did sort in-place we use id
sorted_func = sorted(numbers)
print('Sorted Function id =', id(sorted_func))

print('.sort() method = ', id(numbers))
# compare the above print to another before you use the .sort method and 
# you see that the id's from memory are the same

##############################################################################
# Finding values within a list

# the below is asking id the string physics is in my classes list
# it will return a booleaen value
print('physics' in classes)
print('biology' in classes)
# getting the index position of a certain value in the list. If you know its there
print(classes.index('physics'))

# length of a list
print(len(classes))
#if you want to get the last value in a list you need to add a -1
# because the actual list starts counting at zero but the len function
# starts counting from 1
print(classes[len(classes)-1]) # or print(classes[-1])

##############################################################################
# Min and Max

print(min(numbers))
print(max(numbers))
# with strings it turns it into ascii and uses those numbers values
print(min(classes))
print(max(classes))

##############################################################################
# Counting occurences/duplicates
print(numbers.count(1))

##############################################################################
# Using dir() to output a values built in methods
print(dir(numbers))

