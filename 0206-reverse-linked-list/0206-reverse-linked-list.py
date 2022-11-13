# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = head
        # prev = None
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev
        if head is None or head.next is None:
            return head
        
        rev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return rev