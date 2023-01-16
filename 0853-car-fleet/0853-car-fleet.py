class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        
        stack = []
        cars = [(p, s) for p, s, in zip(position, speed)]
        
        for p, s in sorted(cars)[::-1]:
            t = (target - p)/s
            if not stack or stack[-1] < t:
                stack.append(t)
            
        return len(stack)