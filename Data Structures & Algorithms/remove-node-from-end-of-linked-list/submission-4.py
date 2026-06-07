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

        curr = head
        nu = 0

        while curr:
            if nu == idx:
                curr = curr.next
                nu += 1
                continue

            tail.next = curr
            tail = tail.next
            curr = curr.next
            nu += 1

        tail.next = None

        return dummy.next