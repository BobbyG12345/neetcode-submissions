class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def removeNthFromEnd(self, head, n):
        head = self.reverse(head)

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        # 找到要删除节点的前一个
        for _ in range(n - 1):
            curr = curr.next

        curr.next = curr.next.next

        return self.reverse(dummy.next)