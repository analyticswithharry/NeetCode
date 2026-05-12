// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 075 -- Merge K Sorted Lists
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 38
// =============================================================
//
// QUESTION:
//   Merge k sorted linked lists into one sorted list.
//
//   Example: [[1,4,5],[1,3,4],[2,6]] -> 1->1->2->3->4->4->5->6
// =============================================================

import java.util.*;
public class Lesson075_MergeKSortedLists {
    static class ListNode { int val; ListNode next; ListNode(int v){val=v;} }
    public ListNode mergeKLists(ListNode[] lists){
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a,b)->a.val-b.val);
        for (ListNode n: lists) if (n!=null) pq.add(n);
        ListNode d = new ListNode(0), cur = d;
        while (!pq.isEmpty()){
            ListNode n = pq.poll(); cur.next = n; cur = n;
            if (n.next != null) pq.add(n.next);
        }
        return d.next;
    }
    static ListNode fromArr(int[] a){ ListNode d=new ListNode(0), c=d; for (int x: a){ c.next=new ListNode(x); c=c.next; } return d.next; }
    static List<Integer> toArr(ListNode n){ List<Integer> r=new ArrayList<>(); while (n!=null){ r.add(n.val); n=n.next; } return r; }
    public static void main(String[] a){
        ListNode[] ls = { fromArr(new int[]{1,4,5}), fromArr(new int[]{1,3,4}), fromArr(new int[]{2,6}) };
        System.out.println(toArr(new Lesson075_MergeKSortedLists().mergeKLists(ls)));
    }
}
