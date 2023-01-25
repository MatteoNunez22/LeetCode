class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # My method: O(log(n))
        # l, r = 0, len(nums) - 1
        # while l <= r and nums[l] > nums[r]:
        #     mid = l + (r - l) // 2
        #     if nums[mid] > nums[l]:
        #         l = mid
        #     else:
        #         r = mid
        # return min(nums[l], nums[l+1])
    
        # Neetcode's method: O(log(n))
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l]) 
                break
            
            mid = l + (r - l) // 2
            res = min(res, nums[mid]) 
            
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
                
        return res
        