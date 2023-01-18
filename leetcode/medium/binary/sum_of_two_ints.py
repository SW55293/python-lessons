#Add or Subtract two numbers without using the + plus or
# - minus sign

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