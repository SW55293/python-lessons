# Pattern          = Mod and Bit shift
# Time Complexity  = O(n)
# Space Complexity = O(1)
"""
Input1 = Bit Integer
Return type = Integer
"""
def rob(nums):
       """
       :type nums: List[int]
       :rtype: int
       """
       prev1 = 0
       prev2 = 0
       # start position example
       # [prev1, prev2, n, n+1, n+2, ...]
       for n in nums:
           #we need to choose the greater value to start our process
           temp = max(n + prev1, prev2)
           prev1 = prev2
           prev2 = temp
       return prev2 


'''
def rob(self, nums):

    # Initialize `prev1` and `prev2` to 0.
    prev1 = 0
    prev2 = 0

    # Iterate over the numbers in `nums`.
    for n in nums:

        # Calculate the maximum amount of money that can be robbed from the current house and the first house.
        temp = max(n + prev1, prev2)

        # Update `prev1` and `prev2` to reflect the new maximum amount of money that can be robbed from the first two houses.
        prev1 = prev2
        prev2 = temp

    # Return `prev2`, which is the maximum amount of money that can be robbed from the entire sequence of houses.
    return prev2


'''