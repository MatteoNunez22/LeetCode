class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        islands = 0
        visit = set()
        
        def BFS(r, c):
            queue = collections.deque()
            queue.append((r,c))
            visit.add((r,c))
            while queue:
                row, col = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dirR, dirC in directions:
                    r, c = row + dirR, col + dirC
                    
                    if ((r >= 0 and r < ROWS) and (c >= 0 and c < COLS) and 
                            grid[r][c] == "1" and (r,c) not in visit):
                        queue.append((r,c))
                        visit.add((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    BFS(r, c)
                    islands += 1
                    
        return islands
            
            
        