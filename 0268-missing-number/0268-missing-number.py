class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        
        
        res += len(nums)
        for i in range( len(nums)):
            res += i
            res -= nums[i]
            
        return res