# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        dummy = head
        count = 0

        while dummy:
            dummy = dummy.next
            count += 1

        count -= 1
        res = 0

        while head:
            res += (2**count) * head.val
            count -= 1
            head = head.next

        return res