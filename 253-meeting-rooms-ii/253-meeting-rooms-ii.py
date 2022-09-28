class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:       
        min_heap = []
            
        # sort intervals
        intervals.sort(key=lambda interval: interval[0])
        
        # add first interval
        heapq.heappush(min_heap, intervals[0][1])
        
        # loop remaining intervals
        for interval in intervals[1:]: 
            
            # if top room free, pop it out
            if min_heap[0] <= interval[0]:
                heapq.heappop(min_heap)
    
            # add new interval
            heapq.heappush(min_heap, interval[1])
        
        # return length of heap
        return len(min_heap)