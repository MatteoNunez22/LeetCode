# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        solution = []
        heights = {}
        
        def getHeight(node):
            if not node:
                return -1

            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)
            height = max(leftHeight, rightHeight) + 1

            if height in heights:
                heights[height].append(node.val)
            else:
                heights[height] = [node.val]
            return height
        
        rootHeight = getHeight(root)
        
        h = 0
        while (h <= rootHeight):
            solution.append(heights[h])
            h += 1
            
        return solution
        