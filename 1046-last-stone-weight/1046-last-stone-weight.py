class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            x = -1 * heapq.heappop(heap)
            y = -1 * heapq.heappop(heap)
            if x != y:
                if x > y:
                    x, y = y, x
                heapq.heappush(heap, x - y)
            
        if heap:
            return -1 * heap[0]
        else:
            return 0