def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #take count of every numbers frequency using a dictionary
        #return the top k ammounts

        frequency = {}

        for i in nums:
            if i in frequency:  #if i is in dict then we just add one to the value of the key
                frequency[i] += 1
            #if its not in dict, place it and add 1
            else:
                frequency[i] = 1
                #key & value


        return sorted(frequency, key=frequency.get, reverse=True)[:k]