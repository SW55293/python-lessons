# Pattern          = Using Stack
# Time Complexity  = O(n)
# Space Complexity = O(n)
"""
Input1 = 1 String
Return type = Boolean
"""

def reverseBits(n):
    answer = 0
    for _ in range(32):
        
        answer = (answer << 1) | (n & 1)
        n = n >> 1
 
    return  answer



'''
and_op = n & 1
shift_left = answer << 1
answer = shift_left | and_op
'''
#    # Initialize the reversed number to 0
#         reversed_num = 0
        
#         # Iterate over all 32 bits of the given number
#         for i in range(32):
#             # Left shift the reversed number by 1 and add the last bit of the given number to it
#             reversed_num = (reversed_num << 1) | (n & 1)
#             # To add the last bit of the given number to the reversed number, perform an AND operation with the given number and 1
#             n >>= 1
        
#         # Return the reversed number
#         return reversed_num
     