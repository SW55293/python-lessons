
def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort()
    removed = 0
    prev_end = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prev_end:
            prev_end = end
        else:
            removed += 1
            prev_end = min(end, prev_end)
    return removed