# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 070 -- Remove Nth Node From End of List
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 35
# =============================================================
#
# QUESTION:
#   Remove the nth node from the end of a linked list and return its head.
#
#   Example: head = 1->2->3->4->5, n = 2 -> 1->2->3->5
# =============================================================

class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head); fast = slow = dummy
        for _ in range(n): fast = fast.next
        while fast.next: fast = fast.next; slow = slow.next
        slow.next = slow.next.next
        return dummy.next

def from_list(a):
    d = ListNode(); c = d
    for x in a: c.next = ListNode(x); c = c.next
    return d.next
def to_list(n):
    out = []
    while n: out.append(n.val); n = n.next
    return out

if __name__ == "__main__":
    print(to_list(Solution().removeNthFromEnd(from_list([1,2,3,4,5]), 2)))
