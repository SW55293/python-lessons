# Pattern          = Using Stack
# Time Complexity  = O(n)
# Space Complexity = O(n)
"""
Input1 = 1 String
Return type = Boolean
"""


def isValid(s):
    stack = []
    for paren in s:
        if paren == '(':
            stack.append(')')
        elif paren == '{':
            stack.append('}')
        elif paren == '[':
            stack.append(']')
            #when encountering a closing parentheses we compare it to whats
            #on the stack by running a pop and if they dont match then it's invalid
            #and return false and also if the stack is empty
        elif stack.pop() != paren or not stack: 
            return False
    return not stack
 #return True if stack is empty   

print(isValid('[{(}])'))       
print(ord('{'))
print(ord('}'))

'''
The parenthese have to be found in order meaning
this string will render True = [{()}] because once we get to a 
closing bracket the stack contains all closing brackets in order while
this string will render False = [{(}]) because the order is different and the stack wont line
up with the parentheses left to check in the string
'''