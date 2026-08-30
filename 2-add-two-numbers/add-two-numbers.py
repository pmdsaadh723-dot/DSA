# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = n = ListNode(0)
        hold = 0
        while l1 or l2 or hold:
            hold += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            n.next = n = ListNode(hold % 10)
            hold //= 10
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return root.next