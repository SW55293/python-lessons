def canAttendMeetings(intervals):
        intervals.sort(key = lambda x: x.end)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end: return False
        return True

# ------------------------------------------

def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort()

    for i in range(1, len(intervals)):
      if intervals[i - 1][1] > intervals[i][0]:
        return False

    return True

# ------------------------------------------

def canAttendMeetings(intervals):
        intervals.sort(key=lambda i: i[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False
        return True

# ------------------------------------------

def canAttendMeetings(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x[0])

        for i in xrange(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
