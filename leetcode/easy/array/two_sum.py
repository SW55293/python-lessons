# Pattern          = Sliding Window
# Time Complexity  = 
# Space Complexity = 
"""
Input1 = nums: List[int]
Input2 = target: int
return type = List[int]
"""

def twoSum_ex1(nums, target):
    dictionary = {}

    for n in range(len(nums)):
        if target - nums[n] in dictionary:
            return [dictionary[target - nums[n]], n]
        dictionary[nums[n]] = n


list_of_numbers = [2, 8, 9, 90]
target_number = 10 

print(twoSum_ex1(list_of_numbers, target_number))