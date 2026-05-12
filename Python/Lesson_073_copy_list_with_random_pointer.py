# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 073 -- Copy List With Random Pointer
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 37
# =============================================================
#
# QUESTION:
#   Deep copy a linked list where each node has next and a random pointer that may point to any node or null.
# =============================================================

class Node:
    def __init__(self, v, n=None, r=None): self.val=v; self.next=n; self.random=r
class Solution:
    def copyRandomList(self, head):
        if not head: return None
        m = {}; cur = head
        while cur: m[cur] = Node(cur.val); cur = cur.next
        cur = head
        while cur:
            m[cur].next = m.get(cur.next); m[cur].random = m.get(cur.random); cur = cur.next
        return m[head]

if __name__ == "__main__":
    a = Node(1); b = Node(2); a.next = b; a.random = b; b.random = b
    c = Solution().copyRandomList(a)
    print([(n.val, n.random.val if n.random else None) for n in [c, c.next]])
