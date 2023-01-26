class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = r

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < nums[pivot]:
                    pivot = l
                break
            
            mid = l + (r - l) // 2
            if nums [mid] < nums[pivot]:
                pivot = mid
            
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
                
        if pivot == 0:
            l, r = 0, len(nums) - 1
        elif nums[0] <= target <= nums[pivot - 1]:
            l, r = 0, max(pivot - 1, 0)
        elif nums[pivot] <= target <= nums[len(nums) - 1]:
            l, r = pivot, len(nums) - 1
        else:
            return -1
            
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        return -1
            