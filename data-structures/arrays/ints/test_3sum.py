from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # three pointer
        result = set()
        nums.sort()

        for x in range(len(nums)):
            left = x + 1
            right = len(nums) - 1
            while left < right:
                add = nums[x] + nums[left] + nums[right]
                if add > 0:
                    right -= 1
                elif add < 0:
                    left += 1
                else:
                    result.add((nums[x], nums[left], nums[right]))
                    left += 1

        return result

            
            
            

            
sol = Solution()
nums = [-1,0,1,2,-1,-4]  
print(sol.threeSum(nums))       
            
