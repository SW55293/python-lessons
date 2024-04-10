class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        # set sorts and removes duplicates
        nums = set(nums)

        for x in nums:
            if (x - 1) not in nums:
                count = 1
                while (x + count) in nums:
                    count += 1
                longest = max(longest, count)
        return longest
        