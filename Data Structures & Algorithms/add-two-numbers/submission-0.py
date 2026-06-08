# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ''
        str2 = ''

        while l1:
            str1 += str(l1.val)
            l1 = l1.next

        while l2:
            str2 += str(l2.val)
            l2 = l2.next

        temp = str(int(str1[::-1]) + int(str2[::-1]))
        res = list(map(int, temp[::-1]))

        new = ListNode()
        tail = new

        for num in res:
            tail.next = ListNode(num)
            tail = tail.next

        return new.next