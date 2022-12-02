class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start<=end:
            middle = start + (end - start)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
                
        return -1