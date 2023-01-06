class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numsSet = set(nums)
        
        max_count = 0
        for n in nums:
            if n-1 not in numsSet:
                count = 0
                while (n+count) in numsSet:
                    count += 1
                max_count = max(count, max_count)
                
        return max_count
                    