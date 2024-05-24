from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by the start value

        intervals.sort(key = lambda i: i[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            lst_indx_time = merged[-1][1]

            if start <= lst_indx_time:
                merged[-1][1] = max(lst_indx_time, end)
            else:
                merged.append([start,end])
        return merged
















'''
Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Interval = [1,3]
Start = 1
End = 3
'''