# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 075 -- Merge K Sorted Lists
# Category   : Linked List
# Difficulty : Hard
# Study Plan : Day 38
# =============================================================
#
# QUESTION:
#   Merge k sorted linked lists into one sorted list.
#
#   Example: [[1,4,5],[1,3,4],[2,6]] -> 1->1->2->3->4->4->5->6
# =============================================================

import heapq
class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n
class Solution:
    def mergeKLists(self, lists):
        h = []
        for i, n in enumerate(lists):
            if n: heapq.heappush(h, (n.val, i, n))
        d = ListNode(); cur = d
        while h:
            v, i, n = heapq.heappop(h); cur.next = n; cur = n
            if n.next: heapq.heappush(h, (n.next.val, i, n.next))
        return d.next

def from_list(a):
    d = ListNode(); c = d
    for x in a: c.next = ListNode(x); c = c.next
    return d.next
def to_list(n):
    out = []
    while n: out.append(n.val); n = n.next
    return out

if __name__ == "__main__":
    print(to_list(Solution().mergeKLists([from_list([1,4,5]), from_list([1,3,4]), from_list([2,6])])))
