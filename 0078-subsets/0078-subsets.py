class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = [[]]
        for n in nums:
            new = solution.copy()
            for m in solution:
                new.append(m + [n])
            print(new)
            solution = new.copy()
        
        return solution
            