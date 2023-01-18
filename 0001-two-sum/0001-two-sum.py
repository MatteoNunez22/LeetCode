class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        
        for i, n in enumerate(nums):
            if n in hashset:
                return [hashset[n], i]
            hashset[target - n] = i