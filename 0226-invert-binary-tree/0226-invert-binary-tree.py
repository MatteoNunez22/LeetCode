# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: return None
        
        root.left = self.invertTree(root.left) if root.left else None     
        root.right = self.invertTree(root.right) if root.right else None
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        return root