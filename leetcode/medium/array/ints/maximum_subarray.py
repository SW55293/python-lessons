def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        total = 0

        for x in nums:
            total += x
            result = max(result,total)
            if total < 0:
                total = 0
        return result

