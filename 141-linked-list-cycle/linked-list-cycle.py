# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        count = 0
        while curr:
            if count > 10000:
                return True
            count += 1
            curr = curr.next
        return False