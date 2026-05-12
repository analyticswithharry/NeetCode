// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 076 -- Reverse Nodes in k-Group
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 38
// =============================================================
//
// QUESTION:
//   Reverse the nodes of a linked list k at a time. If fewer than k nodes remain, leave them as-is.
//
//   Example: 1->2->3->4->5, k=2 -> 2->1->4->3->5
// =============================================================

import java.util.*;
public class Lesson076_ReverseNodesInKGroup {
    static class ListNode { int val; ListNode next; ListNode(int v){val=v;} }
    public ListNode reverseKGroup(ListNode head, int k){
        ListNode cur = head; int cnt = 0;
        while (cur != null && cnt < k){ cur = cur.next; cnt++; }
        if (cnt < k) return head;
        ListNode prev = null; cur = head;
        for (int i=0;i<k;i++){ ListNode n = cur.next; cur.next = prev; prev = cur; cur = n; }
        head.next = reverseKGroup(cur, k);
        return prev;
    }
    static ListNode fromArr(int[] a){ ListNode d=new ListNode(0), c=d; for (int x: a){ c.next=new ListNode(x); c=c.next; } return d.next; }
    static List<Integer> toArr(ListNode n){ List<Integer> r=new ArrayList<>(); while (n!=null){ r.add(n.val); n=n.next; } return r; }
    public static void main(String[] a){
        System.out.println(toArr(new Lesson076_ReverseNodesInKGroup().reverseKGroup(fromArr(new int[]{1,2,3,4,5}), 2)));
        System.out.println(toArr(new Lesson076_ReverseNodesInKGroup().reverseKGroup(fromArr(new int[]{1,2,3,4,5}), 3)));
    }
}
