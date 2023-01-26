class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = r

        while l <= r:
            if nums[l] < nums[r]:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            else:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                # Left portion is sorted
                if nums[l] <= nums[mid]:
                    if nums[l] <= target <= nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                # Right portion is sorted
                else:
                    if nums[mid] <= target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
        return -1
            