# Pattern          =  Used A Function To Solve
# Time Complexity  = 
# Space Complexity = 
"""
Input1 = s(string)
Input2 = t(string))
Return type = A (Bool) False or True value
"""


def isAnagram(s, t):
        if len(s) != len(t):
            return False

        #here the sorted() function alphabetizes the 2 strings and if they are
        #equal to each other then we have a valid anagram
        if sorted(s) == sorted(t):
            print(sorted(s), sorted(t))
            return True
        return False

def isAnagram2(s,t):
    if len(s) != len(t):
        return False
    
    #we are going to need 2 empty dicts for keeping
    #track of each strings character count
    s_count = {}
    t_count = {}

    for chars in range(len(s)):
        #here as we go through the array we check each key
        #in the dict and increment its count(value)
        s_count[s[chars]] = s_count.get(s[chars], 0) + 1  #the zero is there for when the char is not in
        t_count[t[chars]] = t_count.get(t[chars], 0) + 1  #the dict(default value) to not get an error
    #return only if they are equal 
    return s_count == t_count




print(isAnagram('car', 'rac'))
print(isAnagram2('car', 'rac'))