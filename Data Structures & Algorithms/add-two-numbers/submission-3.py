# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        carry = 0

        while l1 or l2 or carry:
            add = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry  
            digit = add % 10
            carry = add // 10
            res.next = ListNode(digit)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res = res.next

        return dummy.next