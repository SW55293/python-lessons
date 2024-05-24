from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        merged = [intervals[0]]
        count = 0

        for start, end in intervals[1:]:
            lst_indx_time = merged[-1][1]

            if start < lst_indx_time:  #check for overlap
                count += 1
                merged[-1][1] = min(lst_indx_time, end)  # Merge intervals by updating the end time
            else:
                merged.append([start, end])  # No overlap, add the interval

        return count
