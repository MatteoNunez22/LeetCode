# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iteratively
        # prevNode = None
        # currNode = head
        # while currNode:
        #     nextNode = currNode.next
        #     currNode.next = prevNode
        #     prevNode = currNode
        #     currNode = nextNode
        # return prevNode
    
        # Recursively
        if head is None or head.next is None:
            return head
        
        lastNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return lastNode
        