class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = set(nums)
        
        return len(nums) != len(distinct)