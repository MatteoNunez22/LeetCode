# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxdepth = 1
        stack = [(root,1)]
        while len(stack) > 0:
            visit = stack.pop()
            if visit[0]:
                if visit[1] > maxdepth:
                    maxdepth = max(visit[1], maxdepth)
                if visit[0].left:
                    stack.append((visit[0].left,visit[1]+1))
                if visit[0].right:
                    stack.append((visit[0].right,visit[1]+1))
                    
        return maxdepth