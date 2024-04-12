class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '(':
                stack.append('(')
                stack.append(')')
            elif x == '{':
                stack.append('{')
                stack.append('}')
            elif x == '[':
                stack.append('[')
                stack.append(']')
        if set(s) != set(stack):
            return False
        else:
            return True




sol = Solution()
s = "([)]"
print(sol.isValid(s))



