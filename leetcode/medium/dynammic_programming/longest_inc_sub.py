def lengthOfLIS(nums):
       """
       :type nums: List[int]
       :rtype: int
       """
       if not nums:
           return 0
       longest = [1] * len(nums)
       
       for x in range(1, len(nums)):
           for y in range(x):
               if nums[y] < nums[x]:
                   longest[x] = max(longest[x], longest[y] + 1)
       return max(longest)