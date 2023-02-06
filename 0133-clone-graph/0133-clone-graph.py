"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        copyMap = {}
        
        def build(node):
            if node.val in copyMap:
                return copyMap[node.val]
            
            copy = Node(node.val)
            copyMap[node.val] = copy
            
            for n in node.neighbors:
                copy.neighbors.append(build(n))
                
            return copy
                   
        return build(node)
                    
        
        
        
        
        
        