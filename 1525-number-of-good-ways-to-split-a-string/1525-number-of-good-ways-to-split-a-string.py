class Solution:
    def numSplits(self, s: str) -> int:
        left, right = set(), set()
        num_left, num_right = [], []

        for i in range(len(s)-1):
            if not s[i] in left:
                left.add(s[i])
            num_left.append(len(left))
            if not s[len(s)-1-i] in right:
                right.add(s[len(s)-1-i])
            num_right.append(len(right))
        
        # num_right = num_right[::-1]
        good_splits = 0
        for j in range(len(s)-1):
            if num_left[j] == num_right[-(1+j)]:
                good_splits += 1
                
        return good_splits