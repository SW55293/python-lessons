
def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_prod = nums[0]
    cur_smallest = 1
    cur_biggest = 1
    for n in nums:
        temp = cur_biggest * n
        print('temp = ', temp)
        cur_biggest = max(n * cur_biggest, n * cur_smallest, n)
        print('biggest = ', cur_biggest)
        cur_smallest = min(n * cur_smallest, temp , n)
        print('smallest = ', cur_smallest)
        max_prod = max(max_prod, cur_biggest)
        print('cur max prod = ', max_prod)
        print()
        
    return max_prod

'''
subarrays in [2,3,-2,4]

[2], [2,3], [2,3,-2], [2,3,-2,4]
 2, 6, -12, -48
the min and max in the subarrays for each will change
as you multiply the numbers


will need to loop through and check the numbers right 
next to each other and take the product and compare
with the last product you have
if it is bigger then we have a new high if we dont
keep going
'''

'''
('temp = ', 2)
('biggest = ', 2)
('smallest = ', 2)
('cur max prod = ', 2)
()
('temp = ', 6)
('biggest = ', 6)
('smallest = ', 3)
('cur max prod = ', 6)
()
('temp = ', -12)
('biggest = ', -2)
('smallest = ', -12)
('cur max prod = ', 6)
()
('temp = ', -8)
('biggest = ', 4)
('smallest = ', -48)
('cur max prod = ', 6)
()
'''