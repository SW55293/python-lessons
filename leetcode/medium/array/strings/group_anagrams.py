import collections
def groupAnagrams(strs):
        
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #group the words that have the same letters
        #we want to count the number of letters in each string
        #we're using a hashmap to keep track of the list of lists

        groups = collections.defaultdict(list)

        for word in strs:
            # Sort the string and create a key from the sorted string.
            key = ''.join(sorted(word))
            #for the sorted key place the word in that position
            #if theres already a key with the same sort then add it to that keys list
            groups[key].append(word)

        return groups.values()


# {key = ''.join(sorted(word))} -> Access using the key. If the key does not exist, then a new list will be created for that key
#the key in the dictionary is the sorted strings
#the first unique sorted word is a key 