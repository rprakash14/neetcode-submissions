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
            return 0

        minHeap = []

        intervals.sort(key=lambda x:x.start)

        heapq.heappush(minHeap, intervals[0].end)

        for i in range(1, len(intervals)):
            # If the earliest-ending meeting is done, reuse that room
            if intervals[i].start >= minHeap[0]:
                heapq.heappop(minHeap)
            
            # if earliest ending meeting is still going on, need a new room (implied)
            heapq.heappush(minHeap, intervals[i].end)
        
        return len(minHeap)



        