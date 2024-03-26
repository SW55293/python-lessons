from typing import List

class Solution:
    # This one is a tad slower because of assigning the check variable
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for n in range(len(nums)):
            check = target - nums[n]
            if check in dict:
                return [dict[check], n]
            dict[nums[n]] = n

    # This one is faster without it
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for n in range(len(nums)):

            if target - nums[n] in dict:
                return [dict[target - nums[n], n]]
            dict[nums[n]] = n

    
sol = Solution()

nums = [2, 3, 9 ,5 ,6 ,7, 10]
target = 12

sol.twoSum(nums, target)