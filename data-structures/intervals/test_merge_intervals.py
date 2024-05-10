from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by the start value

        intervals.sort()

















'''
Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Interval = [1,3]
Start = 1
End = 3
'''