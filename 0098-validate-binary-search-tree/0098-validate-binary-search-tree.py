# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, lowLim, highLim):
            if not root:
                return True 
            
            if root.val <= lowLim or root.val >= highLim:
                return False
            
            return isValid(root.left, lowLim, root.val) and isValid(root.right, root.val, highLim)
        
        return isValid(root, float("-INF"), float("INF"))