
def ex_2(nums, target):
    storage = {}

    for x in range(len(nums)):
        remainder = target - nums[x]
        if remainder in storage:
            
            return (storage[remainder], x), ()
        storage[nums[x]] = x

list_of_numbers = [2, 11, 15,7]
target_number = 9

print(ex_2(list_of_numbers, target_number))