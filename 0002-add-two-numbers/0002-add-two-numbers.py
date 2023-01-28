# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        start = ListNode()
        currNode = start
        while l1 and l2:
            value = l1.val + l2.val + carry
            carry = value // 10
            newNode = ListNode(value % 10)
            currNode.next = newNode
            print(value, carry)
            # Update pointers
            l1, l2 = l1.next, l2.next
            currNode = currNode.next
           
        if l1 or l2:
            rest = l1 if l1 else l2
            while rest:
                value = rest.val + carry
                carry = value // 10
                newNode = ListNode(value % 10)
                currNode.next = newNode
                # Update pointers
                rest = rest.next
                currNode = currNode.next
            
        if carry:
            newNode = ListNode(carry)
            currNode.next = newNode
            
        return start.next