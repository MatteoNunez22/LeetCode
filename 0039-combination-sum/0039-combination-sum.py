class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def combinations(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            combinations(i, curr + [candidates[i]], total + candidates[i])
            combinations(i + 1, curr, total)
            
        combinations(0, [], 0)
            
        return res