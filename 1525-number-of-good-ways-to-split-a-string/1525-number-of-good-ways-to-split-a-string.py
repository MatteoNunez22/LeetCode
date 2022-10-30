class Solution:
    def numSplits(self, s: str) -> int:
        left = set()
        num_left = []
        # for i in range(len(s)-1):
        #     if not s[i] in left:
        #         left.add(s[i])
        #     num_left.append(len(left))
        
        right = set()
        num_right = []
        # for i in range(len(s)-1,0,-1):
        #     if not s[i] in right:
        #         right.add(s[i])
        #     num_right.append(len(right))
            
        for i in range(len(s)-1):
            if not s[i] in left:
                left.add(s[i])
            num_left.append(len(left))
            if not s[len(s)-1-i] in right:
                right.add(s[len(s)-1-i])
            num_right.append(len(right))
        
        num_right = num_right[::-1]
        good_splits = 0
        for i in range(len(s)-1):
            if num_right[i] == num_left[i]:
                good_splits += 1
                
        return good_splits