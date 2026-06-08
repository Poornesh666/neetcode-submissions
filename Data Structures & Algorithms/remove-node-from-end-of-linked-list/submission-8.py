class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = fast = dummy

        count = 0

        while count < n:
            count += 1
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

