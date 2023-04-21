class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            
            if stone1 != stone2:
                heapq.heappush(heap, stone1 - stone2)
        
        heap.append(0)
        return abs(heap[0])
                