class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left = [1] * (N)
        prefix = 1
        for i in range(1, N):
            left[i] = prefix * nums[i-1]
            prefix = left[i]
        print(left)
            
        right = [1] * (N)
        suffix = 1
        for i in range(N-2, -1, -1):
            right[i] = suffix * nums[i+1]
            suffix = right[i]
        print(right)
        
        output = [1] * N
        for i in range(0, N):
            output[i] = left[i] * right[i]
        
        return output