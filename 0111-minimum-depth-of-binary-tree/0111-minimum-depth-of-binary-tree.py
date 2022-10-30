# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = [(root, 1)]
        while len(queue) > 0:
            visit = queue.pop(0)
            if visit:
                if visit[0].left is None and visit[0].right is None:
                    return visit[1]
                if visit[0].left:
                    queue.append((visit[0].left, visit[1]+1))
                if visit[0].right:
                    queue.append((visit[0].right, visit[1]+1))
        
        return -1