class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0

        n = len(nums)
        res += n

        for i in range(n):
            res += i
            res -= nums[i]

        return res