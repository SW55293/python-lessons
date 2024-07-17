# Pattern          = Sliding Window
# Time Complexity  = 
# Space Complexity = 
"""
Input1 = nums(List[int]) a list of integers
Input2 = target(int) an integer
Return type = A (List[int]) list of integers 
"""

def twoSum_ex1(nums, target):
    dictionary = {}

    for n in range(len(nums)):
        if target - nums[n] in dictionary:
            return [dictionary[target - nums[n]], n]
        dictionary[nums[n]] = n


list_of_numbers = [2, 11, 15,7]
target_number = 9

# print(twoSum_ex1(list_of_numbers, target_number))

'''
Here's a breakdown of its components:

return: This keyword signals that the function is about to return a value(s) to the calling code.

[ ... ]: These square brackets create a list, which is a collection of ordered elements in Python.

dictionary[target - nums[n]]: This expression accesses a value from a dictionary using a key.

dictionary: This refers to a previously defined dictionary object.

target - nums[n]: This calculates a key to look up within the dictionary.

target: A variable holding a specific value.

nums[n]: Retrieves an element from a list or array called nums at index n.

, n: This adds the value of the variable n as a second element to the list being returned.

'''