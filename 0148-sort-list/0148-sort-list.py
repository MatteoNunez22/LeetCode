# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.getMiddle(head)
        
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
    
    def getMiddle(self, root):
        slow, fast = root, root.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def merge(self, first, second):
        start = ListNode()
        last = start
        while first and second:
            if first.val < second.val:
                last.next = first
                first = first.next
            else:
                last.next = second
                second = second.next
            last.next.next = None
            last = last.next
        
        if first:
            last.next = first
        elif second:
            last.next = second
            
        return start.next
            
            