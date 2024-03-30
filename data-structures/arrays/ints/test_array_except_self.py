from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in nums]
        before = 1
        # calculate left side of x
        for x in range(len(nums)):
            result[x] *= before
            before *= nums[x]
        
        after = 1
        for x in range(len(nums) -1, -1, -1):
            result[x] = result[x] * after
            after *= nums[x]
        
        return result

sol = Solution()
nums = [2,4,8,2]
print(sol.productExceptSelf(nums))