# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 071 -- Reorder List
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 36
# =============================================================
#
# QUESTION:
#   Reorder L0 -> L1 -> ... -> Ln-1 -> Ln to L0 -> Ln -> L1 -> Ln-1 -> ...
#
#   Example: 1->2->3->4 -> 1->4->2->3
# =============================================================

class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n
class Solution:
    def reorderList(self, head):
        if not head or not head.next: return head
        slow = fast = head
        while fast.next and fast.next.next: slow = slow.next; fast = fast.next.next
        prev, cur = None, slow.next; slow.next = None
        while cur: nxt = cur.next; cur.next = prev; prev = cur; cur = nxt
        l1, l2 = head, prev
        while l2:
            t1, t2 = l1.next, l2.next
            l1.next = l2; l2.next = t1
            l1, l2 = t1, t2
        return head

def from_list(a):
    d = ListNode(); c = d
    for x in a: c.next = ListNode(x); c = c.next
    return d.next
def to_list(n):
    out = []
    while n: out.append(n.val); n = n.next
    return out

if __name__ == "__main__":
    print(to_list(Solution().reorderList(from_list([1,2,3,4]))))
    print(to_list(Solution().reorderList(from_list([1,2,3,4,5]))))
