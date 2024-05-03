class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for x in range(len(s)):
            # odd
            count += self.check_palin(s,x,x)
            # even
            count += self.check_palin(s,x,x+1)
        return count

    def check_palin(self, s: str, left: int, right: int):
        local_counter = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            local_counter += 1
            left -= 1
            right += 1
        return local_counter

        
sol = Solution()
s = "aaa"
print(sol.countSubstrings(s))