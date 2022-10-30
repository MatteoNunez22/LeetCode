class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: 
            return 0
        
        nums.sort()
        print(nums)
        min_diff = float('inf')
        w_len = len(nums)-3
        
        for i in range(1,4):
            window = nums[i:i+w_len]
            min_diff = min(min_diff, window[-1]-window[0])
            
        for i in range(1,4):
            window = nums[-i-w_len:-i]
            min_diff = min(min_diff, window[-1]-window[0])
        
        return min_diff