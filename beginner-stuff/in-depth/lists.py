# A more in-depth look into list Method and functions that are built in
'''
Methods vs Functions

Methods are usually of the .method()
example: object.method()

While Functions dont need a dot/period. so function()
example: function(object)
'''

numbers = [15,6,12,5,36,10,1,8,9,10]
classes = ['Comp Sci', 'physics', 'math', 'p.e']

print('UN-Sorted list of Numbers =', numbers)
print('Classes = ', classes)

# sorted() Function
print(sorted(numbers))

# using the .sort() Method | Cant have it inside print function. wont work
numbers.sort()  
print(numbers)

