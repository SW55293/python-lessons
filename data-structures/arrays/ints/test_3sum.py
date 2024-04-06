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
            
# commented
class Solutions:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()  # Initialize an empty set to store the unique triplets.

        nums.sort()  # Sort the input list to enable the two-pointer technique.

        for x in range(len(nums)):  # Iterate through each number in the list.
            left = x + 1  # Initialize the left pointer to the next element.
            right = len(nums) - 1  # Initialize the right pointer to the last element.
            while left < right:  # Keep iterating as long as left is less than right.
                add = nums[x] + nums[left] + nums[right]  # Calculate the sum of the current triplet.
                if add > 0:  # If the sum is greater than zero,
                    right -= 1  # move the right pointer leftwards to reduce the sum.
                elif add < 0:  # If the sum is less than zero,
                    left += 1  # move the left pointer rightwards to increase the sum.
                else:  # If the sum is zero, it's a valid triplet.
                    result.add((nums[x], nums[left], nums[right]))  # Add the triplet to the set to ensure uniqueness.
                    left += 1  # Move the left pointer rightwards to continue searching for other triplets.

        return list(result)  # Convert the set to a list and return the list of unique triplets.
