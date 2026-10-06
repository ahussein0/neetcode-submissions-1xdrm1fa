"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start: # previous end which is [0,30] <--30 vs 5 that means we have an overlap
                return False
        return True


        

