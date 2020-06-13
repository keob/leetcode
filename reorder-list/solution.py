from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return head
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        p = slow.next
        tail = slow.next
        slow.next = None

        p = self.reverseList(p)
        m = head
        while p:
            m.next, p.next, m, p = p, m.next, m.next, p.next

    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
