class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        
        while l <= r and nums[l] > nums[r]:
            mid = l + (r - l) // 2
            print(l, r, mid)
            
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
            
        return min(nums[l], nums[l+1])