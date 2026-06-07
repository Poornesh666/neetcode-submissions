# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        idx = length - n
        nu = -1

        curr = head

        while curr:
            nu += 1
            if nu == idx:
                curr = curr.next
                tail.next = None
                continue
            tail.next = curr
            curr = curr.next
            tail = tail.next

        return dummy.next
