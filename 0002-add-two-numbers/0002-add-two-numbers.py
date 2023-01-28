# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # O(n), O(1)
        carry = 0
        start = ListNode(0)
        currNode = start
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + carry
            carry = value // 10
            newNode = ListNode(value % 10)
            currNode.next = newNode
            # Update pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            currNode = currNode.next
            
        if carry:
            newNode = ListNode(carry)
            currNode.next = newNode
            
        return start.next