# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not (head and head.next):
            return True

        p = ListNode(-1)
        p.next, low, fast = head, p, p

        while fast and fast.next:
            low, fast = low.next, fast.next.next
        cur, pre = low.next, None
        low.next = None

        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        a, b = p.next, pre

        while b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next

        return True
