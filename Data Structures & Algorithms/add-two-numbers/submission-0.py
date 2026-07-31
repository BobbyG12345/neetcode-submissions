# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while curr1 or curr2 or carry:
            x = curr1.val if curr1 else 0
            y = curr2.val if curr2 else 0
            total = x + y + carry
            curr.next = ListNode(total % 10)
            carry = total // 10
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            curr = curr.next
        return dummy.next