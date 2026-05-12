// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 071 -- Reorder List
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 36
// =============================================================
//
// QUESTION:
//   Reorder L0 -> L1 -> ... -> Ln-1 -> Ln to L0 -> Ln -> L1 -> Ln-1 -> ...
//
//   Example: 1->2->3->4 -> 1->4->2->3
// =============================================================

import java.util.*;
public class Lesson071_ReorderList {
    static class ListNode { int val; ListNode next; ListNode(int v, ListNode n){val=v; next=n;} }
    public void reorderList(ListNode head){
        if (head==null || head.next==null) return;
        ListNode slow=head, fast=head;
        while (fast.next!=null && fast.next.next!=null){ slow=slow.next; fast=fast.next.next; }
        ListNode prev=null, cur=slow.next; slow.next=null;
        while (cur!=null){ ListNode n=cur.next; cur.next=prev; prev=cur; cur=n; }
        ListNode l1=head, l2=prev;
        while (l2!=null){ ListNode t1=l1.next, t2=l2.next; l1.next=l2; l2.next=t1; l1=t1; l2=t2; }
    }
    static ListNode fromArr(int[] a){ ListNode d=new ListNode(0,null), c=d; for (int x: a){ c.next=new ListNode(x,null); c=c.next; } return d.next; }
    static List<Integer> toArr(ListNode n){ List<Integer> r=new ArrayList<>(); while (n!=null){ r.add(n.val); n=n.next; } return r; }
    public static void main(String[] a){
        ListNode h = fromArr(new int[]{1,2,3,4}); new Lesson071_ReorderList().reorderList(h); System.out.println(toArr(h));
        ListNode h2 = fromArr(new int[]{1,2,3,4,5}); new Lesson071_ReorderList().reorderList(h2); System.out.println(toArr(h2));
    }
}
