# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = ListNode(-1)
        node.next, a, b = head, node, node
        while n > 0 and b:
            b, n = b.next, n - 1

        if not b:
            return head

        while b.next:
            a, b = a.next, b.next

        a.next = a.next.next

        return node.next
