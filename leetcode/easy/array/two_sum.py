#  Find the numbers that up to the Target number.
#  If found return the indices of the two numbers that
#  add up to that target number

def twoSum_ex1(nums, target):
    dictionary = {}

    for n in range(len(nums)):
        if target - nums[n] in dictionary:
            return [dictionary[target - nums[n]], n]
        dictionary[nums[n]] = n


list_of_numbers = [2, 8, 9, 90]
target_number = 10 

print(twoSum_ex1(list_of_numbers, target_number))