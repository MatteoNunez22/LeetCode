class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Sliding window + deque: O(n), O(n)
        res = []
        deque = collections.deque()

        l = 0    
        for r in range(len(nums)):
            # Validate deque
            while deque and nums[r] > nums[deque[-1]]:
                deque.pop()
            
            # Add new value
            deque.append(r)
            
            # Pop leftmost value
            if deque[0] < l:
                deque.popleft()
            
            if r + 1 >= k:
                res.append(nums[deque[0]])
                l += 1
        
        return res