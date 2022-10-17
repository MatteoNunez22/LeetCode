class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda interval: interval[0])
        
        minheap = []
        count = 0
        for interval in intervals:
            if minheap and minheap[0] <= interval[0]:
                heapq.heappushpop(minheap, interval[1])
            else:
                heapq.heappush(minheap, interval[1])
                count += 1
        
        return count