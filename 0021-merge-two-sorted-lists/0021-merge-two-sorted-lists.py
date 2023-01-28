# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        head = ListNode()
        prev = head
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev.next = curr1
                prev = curr1
                curr1 = curr1.next
            else:
                prev.next = curr2
                prev = curr2
                curr2 = curr2.next
        
        if curr1 is None:
            prev.next = curr2 
        elif curr2 is None:
            prev.next = curr1
        
        return head.next
        
        