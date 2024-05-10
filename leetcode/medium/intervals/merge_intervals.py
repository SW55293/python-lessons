
def merge(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #sort by the start value
        intervals.sort(key = lambda i: i[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_indexed = merged[-1][1]

            if start <= last_indexed:
                #merge
                merged [-1][1] = max(last_indexed,end)
            else: 
                merged.append([start,end])

        return merged

#All cases + edge cases (after they are sorted by start number)
#1. [1,4], [2,3] the first intervals end is bigger than the seconds
#2. [1,2], [1,2] all intervals are the same
#3. [4,5], [5,9] the end of the next interval is bigger