from typing import List

def findMin(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        middle = (left + right) // 2
        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle
    return nums[left]

'''
def findMin(self, nums: List[int]) -> int:
        # Initialize the left and right pointers.
        # left: The index of the smallest number in the array.
        # right: The index of the largest number in the array.
        left = 0
        right = len(nums) - 1

        # While the left pointer is less than the right pointer,
        # keep searching for the smallest number in the array.
        while left < right:
            # Calculate the middle index.
            mid = (left + right) // 2

            # If the number at the middle index is greater than the number at the right index,
            # then the minimum number must be in the right half of the array.
            # So, update the left pointer to the middle index + 1.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum number must be in the left half of the array.
            # So, update the right pointer to the middle index.
            else:
                right = mid

        # Return the number at the left pointer.
        # This is the smallest number in the array.
        return nums[left]


'''