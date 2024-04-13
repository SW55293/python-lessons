class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # key is the closing paren
        all_pairs = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for x in s:
            # if a opening paren is found add to stack
            if x in all_pairs:
                 stack.append(x)
            # if the len of stack is 0 or if the closing bracket doesnt match with the last opening value
            # added to the stack when using the all_pairs matching map then return false
            elif len(stack) == 0 or x != all_pairs[stack.pop()]:
                 return False

        return len(stack) == 0

sol = Solution()
s = "(&[)]"
print(sol.isValid(s))



