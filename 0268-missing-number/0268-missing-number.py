class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        for i in range(n):
            res += i
        
        for i in range(n):
            res -= nums[i]
            
        return res