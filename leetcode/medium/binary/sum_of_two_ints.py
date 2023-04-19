#Add or Subtract two numbers without using the + plus or
# - minus sign

def sum_of_two(a,b):
    bitShortener = 0xffffffff

    while b & bitShortener > 0:
          carry = (a & b) << 1 
          a = a ^ b
          b = carry
    return (a & bitShortener) if b > 0 else a


'''
bitShortener will never change its value it will always be 32 1's

in python ints are stored as 256 bits so we want to
shorten that to use only 32 bits because we only need 32 bits
in binary 0xffffffff = 11111111111111111111111111111111
'''





# =====================================================

def add_without_sign(a, b):

    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
print(add_without_sign(1, 4))

#example
# 1 in binary = 0001
# 4 in binary = 0100
# Add them in binary
# 
# 0001
# 0100
# ----
# 0101 = 5 

'''
The function uses a bitwise approach to perform addition of two numbers without using the '+' operator. 
The bitwise operator "&" performs bitwise AND operation and "^" performs bitwise XOR operation.

The function first checks if there is any carry from the previous addition by performing bitwise
AND operation on the two integers "a" and "b". If there is any carry, it is stored in the variable 
"carry". The value of "a" is then updated by performing bitwise XOR operation on "a" and "b". The value of 
"b" is updated by shifting the value of "carry" to the left by one position using the bitwise operator "<<". 
This is done to add the carry to the next significant bit.

The process is repeated until there is no carry left. At this point, the value of "a" contains the sum of "a" and "b", 
which is returned by the function.

Overall, this function implements a binary addition algorithm using bitwise operations to calculate the sum of two
integers without using the '+' operator.


'''