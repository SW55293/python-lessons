# Pattern          = Math Equation
# Time Complexity  = O(n)
# Space Complexity = O(1)
"""
Input1 = Array/List of Integers
Return type = 1 Integer
"""

def missingNumber(nums):

    len_of_nums = len(nums)
    sum_of_nums = sum(nums)

    return (len_of_nums + 1)*(len_of_nums)//2 - sum_of_nums
	



# explanation -> [ 0 , 1 , 3 ]: sum = 4 and length = 3
# We can see that 2 is missing 
# So we add length of nums to account for a missing number
# and divide 3 by 2 and subtract it by the sum
'''
length_of_nums     -> (3 + 1)
length_of_nums / 2 -> 3/2
sum_of_nums        -> 4
-> (4) * 3/2 - 4
-> 6 - 4 = 2
'''


'''
Since we know the values of the array are from 0 to n with one missing number and the indexes are from 0 to n-1, 
we can use a sum of the these values and indexes to find the missing number. You first initialize the sum to n because you can’t 
reach that value through iteration, then iterate through the array and add the sum of the index minus the value
'''