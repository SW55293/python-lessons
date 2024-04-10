from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        most_water = 0

        while left < right:
            curr_height = 0
            diff = right - left

            if height[left] > height[right]:
                curr_height = diff * height[right]
            elif height[right] > height[left]:
                curr_height = diff * height[left]
            else:
                smallest = min(height[left], height[right])
                curr_height = diff * smallest

            most_water = max(most_water, curr_height)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return most_water