"""
Input1 = Integer List
Return type = Boolean
"""

# Pattern          = Map/Dictionary Copy
# Time Complexity  = O(n)
# Space Complexity = O(n)
# 1
def containsDuplicate(nums):

    dict = {}

    for x in nums:
        if nums[x] in dict:
            return True
        dict[nums[x]] = x

    return False
print(containsDuplicate([1,2,3,3]))

# Pattern          = Sort and Compare Length
# Time Complexity  = O(n)
# Space Complexity = O(n)
# 2
def containsDuplicate2(nums):
    nums.sort()

    for i in range(len(nums)-1):   # or just for i in nums: works
        if nums[i] == nums[i+1]: return True
    return False
print(containsDuplicate2([1,2,3,3]))

# Pattern          = Set & Len Function Comparing
# Time Complexity  = O(n)
# Space Complexity = O(n)
# 3
def containsDuplicate3(nums):
    return len(set(nums)) != len(nums)
    #or len(nums) > len(set(nums)) 