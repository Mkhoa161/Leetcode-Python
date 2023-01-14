# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        # None <- 1 <- 2 <- 3 
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

                
