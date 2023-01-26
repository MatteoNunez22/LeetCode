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
                
                if nums[l] <= nums[mid]:
                    if not (nums[l] <= target <= nums[mid]):
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if not (nums[mid] <= target <= nums[r]):
                        r = mid - 1
                    else:
                        l = mid + 1

        return -1
            