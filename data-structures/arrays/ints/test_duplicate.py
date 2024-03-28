from typing import List
from icecream import ic

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return f'True, We do have duplicates'
            seen.add(x)                 
        return False

  

    def containsDuplicate2(self, nums: List[int]) -> bool:
        dict = {}

        for x in range(len(nums)):
            if nums[x] in dict:
                return True
            dict[nums[x]] = x
        return False
    
sol = Solution()

nums = [1,2,3,1,2,3]
# ic(sol.containsDuplicate(nums))

print(sol.containsDuplicate(nums))
