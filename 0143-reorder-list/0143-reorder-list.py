# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Get middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        # Reverse right half
        prev = None
        currNode = mid
        while currNode:
            nextNode = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = nextNode

        left, right = head, prev
        while right:
            leftNext = left.next
            rightNext = right.next
            left.next = right
            right.next = leftNext
            left = leftNext
            right = rightNext

        
        