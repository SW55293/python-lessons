
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counts = [0] * 26  # Assuming lowercase letters a-z

        for char in s:
            char_counts[ord(char) - ord('a')] += 1

        for char in t:
            char_counts[ord(char) - ord('a')] -= 1
            if char_counts[ord(char) - ord('a')] < 0:
                return False

        return True

sol = Solution()
s = "things"
t = "phings"
print(sol.isAnagram(s,t))