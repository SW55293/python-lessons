# Bit manipulation is needed for cases when arithmetic operators cannot
# be used
# 1 = True
# 2 = False
# AND = &   [0 & 0 = 0 || 0 & 1 = 0 || 1 & 1 = 1 ]
# OR  = |   [1 | 0 = 1 || 0 | 0 = 0 || 1 | 1 = 1 ]
# XOR = ^   [1 | 0 = 1 || 0 | 0 = 0 || 1 | 1 = 1 ]
# NOT = ~   [~1 = 1]
# Shift Left  = <<
# Shift Right = >>


#using bin() we can get the binary representation
a = 45
b = 10
print(bin(a))
print(bin(b))
#the output gives us a 0b that is not necessary so we can remove like so
print(bin(a)[2:])
print(bin(b)[2:])
print()
first_num = 6
second_num = 4

and_op = first_num & second_num
or_op = first_num | second_num
not_op = ~first_num
xor_op = first_num ^ second_num

# AND
print('6 & 4 = ', and_op)
# 6 = 0110
# 4 = 0100
# + --------
#     0100 and 0100 = 4 

# OR
print('6 | 4 = ', or_op)

# NOT
print('~6 NOT = ', not_op)

# XOR
print('6 ^ 4 = ', xor_op)

# this shift left appends 1 0 to the end of binary 10
# so originally you have
# 10 = 0000 1010
#then= 0001 0100
#and 0001 0100 = 20
print(10 << 1 )


#Practice
#  while (y != 0):
     
#         # carry now contains common
#         # set bits of x and y
#         carry = x & y
 
#         # Sum of bits of x and y where at
#         # least one of the bits is not set
#         x = x ^ y
 
#         # Carry is shifted by one so that  
#         # adding it to x gives the required sum
#         y = carry << 1
     
#     return x



def adding_without_plus(a, b):
    while b !=0:
        carry = a & b
        print(f'carry = {carry}, a = {a}, b = {b}')

        a = a ^ b
        print(f'carry = {carry}, a = {a}, b = {b}')

        b = carry << 1
        print(f'carry = {carry}, a = {a}, b = {b}')
        print()
    return a

print(adding_without_plus(100,100))