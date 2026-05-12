# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 003 -- Reverse Linked List
# Category   : Linked List
# Difficulty : Easy
# Study Plan : Day 2
# =============================================================
#
# QUESTION:
#   Given the head of a singly linked list, reverse the list and return
#   the new head.
#
#   Example:
#     Input : 1 -> 2 -> 3 -> 4 -> 5
#     Output: 5 -> 4 -> 3 -> 2 -> 1
# =============================================================

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val, self.next = val, nxt

class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev

def to_list(h):
    out = []
    while h: out.append(h.val); h = h.next
    return out

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(to_list(Solution().reverseList(head)))  # [5,4,3,2,1]
