class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        if len(edges) == 1:
            return n - 1
        
        adjMap = collections.defaultdict(list)
        
        for a, b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
        
        connectCount = 0
        visitSet = set()
        
        def dfs(node):
            if node in visitSet:
                return False
            
            visitSet.add(node)
            for adjNode in adjMap[node]:
                dfs(adjNode)
                
            return True

        for i in range(n):
            if dfs(i):
                connectCount += 1
            
        return connectCount
        