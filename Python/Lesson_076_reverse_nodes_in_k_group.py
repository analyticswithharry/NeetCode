# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 076 -- Reverse Nodes in k-Group
# Category   : Linked List
# Difficulty : Hard
# Study Plan : Day 38
# =============================================================
#
# QUESTION:
#   Reverse the nodes of a linked list k at a time. If fewer than k nodes remain, leave them as-is.
#
#   Example: 1->2->3->4->5, k=2 -> 2->1->4->3->5
# =============================================================

class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n
class Solution:
    def reverseKGroup(self, head, k):
        cur = head; cnt = 0
        while cur and cnt < k: cur = cur.next; cnt += 1
        if cnt < k: return head
        prev, cur = None, head
        for _ in range(k):
            nxt = cur.next; cur.next = prev; prev = cur; cur = nxt
        head.next = self.reverseKGroup(cur, k)
        return prev

def from_list(a):
    d = ListNode(); c = d
    for x in a: c.next = ListNode(x); c = c.next
    return d.next
def to_list(n):
    out = []
    while n: out.append(n.val); n = n.next
    return out

if __name__ == "__main__":
    print(to_list(Solution().reverseKGroup(from_list([1,2,3,4,5]), 2)))
    print(to_list(Solution().reverseKGroup(from_list([1,2,3,4,5]), 3)))
