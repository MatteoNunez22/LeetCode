class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def combinations(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            combinations(i, curr, total + candidates[i])
            curr.pop()
            combinations(i + 1, curr, total)
            
        combinations(0, [], 0)
            
        return res