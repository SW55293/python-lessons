#Lambdas are a bit like anonymous function
#Usually used when you need a one time use function
#Single Use

nums = [1,2,3,6,45,45,77]

def square_the_numbers(n):
    return n * n

print(list(map(square_the_numbers, nums)))

#Say we were only going to use the square_the_numbers function once
#we could use a lambda function instead
#####################

print(list(map(lambda n: n * n, nums)))