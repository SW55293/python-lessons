
# Pattern          = Bit Operation and XOR
# Time Complexity  = O(n)
# Space Complexity = O(1)
"""
Input 1 = Integer Array/List
Return type = 1 Integer
"""

def singleNumber(nums):

    single_num = 0

    for number in nums:
        # print('number = ', number)
        # print('single number before =', single_num)
        # print('XOR =' , single_num ^ number)
       
        single_num = single_num ^ number
       
        # print('single number after =', single_num)
        # print('\n')

    return single_num




print('answers = ', singleNumber([2,2,1,8,9,9]))

# For this we have to find the number that doesnt have a pair
'''XOR
A|B|Output
0|0|0
0|1|1
1|0|1
1|1|0
'''

'''
it turns the numbers into their bit significance
                           8421
0 ^ 2 = 2 -> 0000 ^ 0010 = 0010
2 ^ 2 = 0 -> 0010 ^ 0010 = 0000
0 ^ 1 = 1 -> 0000 ^ 0001 = 0001

'''