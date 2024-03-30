from typing import List
from icecream import ic

    
class Solution:
    def maxProduct2(self, nums: List[int]) -> int:
        
        max_val, min_val = 1,1
        result = nums[0]

        for n in nums:
            max_prod = max_val * n
            min_prod = min_val * n

            max_val = max(min_prod, max_prod, n)
            min_val = min(min_prod, max_prod, n)

            result= max(result, max_val)
        
        return result
    
sol = Solution()
nums = [-2, 3, -4]
ic(sol.maxProduct2(nums))











class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the maximum product,
        # current minimum product, and current maximum product
        res = nums[0]  # Initialize the result with the first element of the array
        curMin, curMax = 1, 1  # Initialize current minimum and maximum product to 1
        
        # Iterate through each number in the array
        for n in nums:
            # Calculate the temporary maximum product considering the current maximum product
            temp_max = curMax * n
            temp_min = curMin * n
            

            curMax = max(temp_max, temp_min, n)

            curMin = min(temp_max, temp_min, n)
            
            # Update the result with the maximum of the current maximum product and the result
            res = max(res, curMax)
        
        # Return the maximum product
        return res