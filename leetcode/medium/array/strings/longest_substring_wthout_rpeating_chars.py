def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        noDuplicates = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in noDuplicates:
                noDuplicates.remove(s[left])
                left = left + 1
            noDuplicates.add(s[right])
            result = max(result, right - left + 1)
            print(noDuplicates)
        return result