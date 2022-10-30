class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: 
            return 0
        
        nums.sort()
        min_diff = float('inf')
        
        w_len = len(nums)-3
        for i in range(1,4):
            min_diff = min(min_diff, nums[i+w_len-1]-nums[i])
            min_diff = min(min_diff, nums[-i-1]-nums[-i-w_len])
        
        return min_diff