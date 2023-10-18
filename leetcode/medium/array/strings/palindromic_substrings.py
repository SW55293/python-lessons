class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        for x in range(len(s)):
            #odd strings/palindromes
            ans += self.pal_pointer(s, x, x)  #(left,right)
            #even strings/palindromes   
            ans += self.pal_pointer(s, x, x + 1)

        return ans

    def pal_pointer(self, s, left, right):
      counter = 0

      while left >= 0 and right < len(s) and s[left] == s[right]:
        counter += 1
        left -= 1
        right += 1

      return counter