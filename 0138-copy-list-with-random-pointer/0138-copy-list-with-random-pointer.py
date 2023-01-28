"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = { None : None}
        
        currNode = head
        while currNode:
            copyNode = Node(currNode.val)
            copyMap[currNode] = copyNode
            currNode = currNode.next
            
        currNode = head
        while currNode:
            copyNode = copyMap[currNode]
            copyNode.next = copyMap[currNode.next]
            copyNode.random = copyMap[currNode.random]
            currNode = currNode.next
            
        return copyMap[head]
        