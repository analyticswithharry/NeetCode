# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 069 -- Add Two Numbers
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 35
# =============================================================
#
# QUESTION:
#   Two non-empty linked lists representing non-negative integers in reverse order. Return sum as linked list.
#
#   Example: 2->4->3 + 5->6->4 = 7->0->8 (i.e., 342 + 465 = 807)
# =============================================================

class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(); cur = dummy; carry = 0
        while l1 or l2 or carry:
            x = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, d = divmod(x, 10); cur.next = ListNode(d); cur = cur.next
            l1 = l1.next if l1 else None; l2 = l2.next if l2 else None
        return dummy.next

def to_list(n):
    out = []
    while n: out.append(n.val); n = n.next
    return out
def from_list(a):
    dummy = ListNode(); cur = dummy
    for x in a: cur.next = ListNode(x); cur = cur.next
    return dummy.next

if __name__ == "__main__":
    print(to_list(Solution().addTwoNumbers(from_list([2,4,3]), from_list([5,6,4]))))
