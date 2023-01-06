class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        
        for n in nums:
            if n-1 not in nums_set:
                count = 0
                while (n+count) in nums_set:
                    count += 1
                max_count = max(count, max_count)
                
        return max_count
                    