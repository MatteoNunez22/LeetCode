# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            hashset = set()
            node = head
            while node.next:
                if node in hashset:
                    return True
                else:
                    hashset.add(node)
                node = node.next
        return False