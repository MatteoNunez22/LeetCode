class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set(nums)
        return len(nums) != len(hashset)