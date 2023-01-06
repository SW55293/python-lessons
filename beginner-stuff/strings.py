#two ways to initialize a string
print('single quotes')
print("double quotes")

# storing, then printing and getting a position in the string
greet = "hello"
print(greet, greet[0])

#Slice/Split a string
cut = "thisword"
print(cut[0:4])
print(cut[4:9])


#Concatenating 2 strings
fname = "Stephanie"
lname = "Walker"
print(fname + ' ' + lname)

#Reapeating a string by multiplying
print(fname*4)

# Uppercase & lowercase
uppr = "make upper"
lwr = "MAKE LOWER"
print(uppr.upper() +" " + lwr.lower())

# List of strings and split on the comma
cheese = "cheddar, pepper jack, colby jack"
print(cheese.split(','))

#Find length of a string
print(len(greet))
print(len(lname))