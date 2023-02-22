# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS: O(n), O(n)
        maxD = [0]  # Use list to avoid error

        def dfs(node):
            if not node:
                return -1
            
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            maxD[0] = max(maxD[0], leftDepth + rightDepth + 2)
            
            return max(leftDepth, rightDepth) + 1
           
        dfs(root)
        
        return maxD[0]