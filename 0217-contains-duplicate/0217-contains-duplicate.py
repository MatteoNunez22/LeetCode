class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Approach 1
        # distinct = set(nums)
        # return len(nums) != len(distinct)
    
        # Approach 2
        l = set()
        for num in nums:
            if num in l:
                return True
            else:
                l.add(num)
        return False
        