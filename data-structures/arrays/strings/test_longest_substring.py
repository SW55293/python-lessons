class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # we increment the end to go off and do the checking
        # if we hit a duplicate we take note of the current max
        # and reinitialize the start to the current duplicate and keep checking
        start = 0
        end = 0
        longest = 0
        dict = {}
        curr = 0

        while end < len(s):
            
            if s[end] not in dict:
                dict[s[end]] = 1
                end += 1
                curr += 1
            else:
                start = end
                end += 1
                dict[s[start]] += 1
                longest = max(longest, curr)
                curr = 0
        return longest



            
       


        