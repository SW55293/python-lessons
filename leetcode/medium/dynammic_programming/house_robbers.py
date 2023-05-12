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
