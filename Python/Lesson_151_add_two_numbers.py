# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 151 -- Add Two Numbers
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 76
# =============================================================
#
# QUESTION:
#   Two non-empty linked lists (least-significant-digit first). Add and return sum as linked list.
# =============================================================
class LN:
    def __init__(self,v,n=None): self.val=v; self.next=n
def add(a,b):
    d=LN(0); cur=d; c=0
    while a or b or c:
        v=c+(a.val if a else 0)+(b.val if b else 0)
        c,v=divmod(v,10)
        cur.next=LN(v); cur=cur.next
        a=a.next if a else None; b=b.next if b else None
    return d.next

def to_list(n):
    o=[]
    while n: o.append(n.val); n=n.next
    return o
def from_list(a):
    d=LN(0); cur=d
    for x in a: cur.next=LN(x); cur=cur.next
    return d.next

if __name__=="__main__":
    print(to_list(add(from_list([2,4,3]),from_list([5,6,4]))))
