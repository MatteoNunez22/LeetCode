class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        idx = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeros += 1
                idx = i
                
        ans = [0] * len(nums)
        print(zeros)
        if zeros >= 2:
            return ans
        elif zeros == 1:
            ans[idx] = product
            return ans
        else:
            for i in range(len(ans)):
                ans[i] = product // nums[i]
            return ans