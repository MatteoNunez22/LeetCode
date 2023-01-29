# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        dummy = ListNode(0, head)
        start = dummy
        
        while True:
            kNode = self.getKth(start, k)
            if not kNode:
                break
            end = kNode.next
            
            prev = end
            curr = start.next
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            temp = start.next
            start.next = kNode
            start = temp
        
        return dummy.next
        