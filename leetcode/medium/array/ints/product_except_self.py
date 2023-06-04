def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #new list
        result = [1] * (len(nums))

        before = 1
        for n in range(len(nums)):
            result[n] = before
            before *= nums[n]

        after = 1
        for n in range(len(nums) -1, -1, -1):
            result[n] *= after
            after *= nums[n]
        return result


'''
nums =   [2,2,4,3]
result = [1,1,1,1]

calculating first for loop: before
before = 1, 2, 4, 16, 48 
result = [1,2,4,16]

calculating second for loop: after
after = 1, 3, 12, 24, 48
result= [24,24,12,16]

24,24,12,16
'''