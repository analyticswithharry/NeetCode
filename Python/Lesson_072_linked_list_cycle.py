# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 072 -- Linked List Cycle
# Category   : Linked List
# Difficulty : Easy
# Study Plan : Day 36
# =============================================================
#
# QUESTION:
#   Determine if a linked list has a cycle. Floyd's tortoise and hare.
# =============================================================

class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n
class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next; fast = fast.next.next
            if slow is fast: return True
        return False

if __name__ == "__main__":
    a = ListNode(1); b = ListNode(2); c = ListNode(3)
    a.next = b; b.next = c; c.next = a
    print(Solution().hasCycle(a))
    d = ListNode(1); d.next = ListNode(2)
    print(Solution().hasCycle(d))
