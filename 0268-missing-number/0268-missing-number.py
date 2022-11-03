class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        present = set(range(len(nums)+1))
        for num in nums:
            present.remove(num)
            
        return present.pop()