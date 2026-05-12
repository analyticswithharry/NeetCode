# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 004 -- Merge Two Sorted Lists
# Category   : Linked List
# Difficulty : Easy
# Study Plan : Day 2
# =============================================================
#
# QUESTION:
#   You are given the heads of two sorted linked lists list1 and list2.
#   Merge them into one sorted list and return its head.
#
#   Example:
#     Input : 1->2->4, 1->3->4
#     Output: 1->1->2->3->4->4
# =============================================================

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val, self.next = val, nxt

class Solution:
    def mergeTwoLists(self, a, b):
        dummy = tail = ListNode()
        while a and b:
            if a.val <= b.val: tail.next, a = a, a.next
            else:              tail.next, b = b, b.next
            tail = tail.next
        tail.next = a or b
        return dummy.next

def build(vs):
    d = ListNode(); t = d
    for v in vs: t.next = ListNode(v); t = t.next
    return d.next

def to_list(h):
    out = []
    while h: out.append(h.val); h = h.next
    return out

if __name__ == "__main__":
    print(to_list(Solution().mergeTwoLists(build([1,2,4]), build([1,3,4]))))
