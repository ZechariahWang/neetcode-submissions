"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        lastEnd=intervals[0].end

        for i in intervals[1:]:
            start=i.start
            end=i.end
            if start<lastEnd:
                return False
        return True
