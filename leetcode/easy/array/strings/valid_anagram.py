import collections

def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :return type: bool
        """
        if len(s) != len(t):
            return False

        #here the sorted() function alphabetizes the 2 strings and if they are
        #equal to each other then we have a valid anagram
        if sorted(s) == sorted(t):
            print(sorted(s), sorted(t))
            return True
        return False

print(isAnagram('car', 'rac'))