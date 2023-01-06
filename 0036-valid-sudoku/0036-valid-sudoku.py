class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        blocks = collections.defaultdict(set)
        
        for x in range(len(board)):
            for y in range(len(board)):
                num = board[y][x]
                if num != ".":
                    if (num in rows[y]) or (num in cols[x]) or (num in blocks[(y//3,x//3)]):
                            return False
                    else:
                        rows[y].add(num)
                        cols[x].add(num)
                        blocks[(y//3,x//3)].add(num)
        
        return True