from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0

        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow = slow + 1
                nums[slow] = nums[fast]
            
        return slow + 1
                
        





'''
slow = 0, fast = 0:
arr[0] != arr[0] is False (duplicate), so no action taken.
fast = 1:
arr[1] != arr[0] is False (duplicate), so no action taken.
fast = 2:
arr[2] != arr[0] is True (unique), so slow becomes 1 and arr[1] is overwritten with 2.
fast = 3:
arr[3] != arr[1] is False (duplicate), so no action taken.
fast = 4:
arr[4] != arr[1] is True (unique), so slow becomes 2 and arr[2] is overwritten with 3.

'''