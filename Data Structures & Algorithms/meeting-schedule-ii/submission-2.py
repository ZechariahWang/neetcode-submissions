"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 1

        numDays=1
        intervals.sort(key=lambda x:x.start)
        lastEnd=intervals[0].end

        for i in intervals[1:]:
            start=i.start
            end=i.end
            if start<=lastEnd:
                numDays+=1
            lastEnd=end

        
        return numDays
