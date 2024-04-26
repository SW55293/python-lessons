class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict = {}
        start = 0
        longest = 0
        result = 0
        
        # end = 0 -> len(s)
        for end in range(len(s)):
            dict[s[end]] = dict.get(s[end], 0) + 1
            longest = max(longest, dict[s[end]])

            if k < (end - start + 1) - longest:
                dict[s[start]] -= 1
                start += 1
            result = max(result, end-start+1)
        return result
    
# another option is to use defaultdict to automatically fill the key value with zeros
from collections import defaultdict
# using defaultdict just initializes all value keys to 0
# so the extra step of running the .get value is not needed
# and speeds up the code 
# dict[s[end]] = dict.get(s[end], 0) + 1
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict = defaultdict(int)
        start = 0
        longest = 0
        result = 0
        
        # end = 0 -> len(s)
        for end in range(len(s)):
            dict[s[end]] += 1          
            longest = max(longest, dict[s[end]])

            if k < (end - start + 1) - longest:
                dict[s[start]] -= 1
                start += 1
            result = max(result, end-start+1)
        return result