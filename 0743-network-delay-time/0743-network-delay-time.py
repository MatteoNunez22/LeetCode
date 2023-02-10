class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # O(E * logV)
        adjList = collections.defaultdict(list)
        
        for u, v, w in times:
            adjList[u].append((v, w))
            
        minHeap = [(0, k)]
        visitSet = set()
        res = 0
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visitSet:
                continue
            visitSet.add(n1)
            res = max(res, w1)
            for n2, w2 in adjList[n1]:
                if n2 not in visitSet:
                    heapq.heappush(minHeap, (w1 + w2, n2))
            
        return res if len(visitSet) == n else -1