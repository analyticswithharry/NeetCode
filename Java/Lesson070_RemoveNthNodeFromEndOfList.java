// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 070 -- Remove Nth Node From End of List
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 35
// =============================================================
//
// QUESTION:
//   Remove the nth node from the end of a linked list and return its head.
//
//   Example: head = 1->2->3->4->5, n = 2 -> 1->2->3->5
// =============================================================

import java.util.*;
public class Lesson070_RemoveNthNodeFromEndOfList {
    static class ListNode { int val; ListNode next; ListNode(int v, ListNode n){val=v; next=n;} }
    public ListNode removeNthFromEnd(ListNode head, int n){
        ListNode d = new ListNode(0, head); ListNode fast=d, slow=d;
        for (int i=0;i<n;i++) fast = fast.next;
        while (fast.next != null){ fast = fast.next; slow = slow.next; }
        slow.next = slow.next.next; return d.next;
    }
    static ListNode fromArr(int[] a){ ListNode d=new ListNode(0,null), c=d; for (int x: a){ c.next = new ListNode(x,null); c=c.next; } return d.next; }
    static List<Integer> toArr(ListNode n){ List<Integer> r=new ArrayList<>(); while (n!=null){ r.add(n.val); n=n.next; } return r; }
    public static void main(String[] a){ System.out.println(toArr(new Lesson070_RemoveNthNodeFromEndOfList().removeNthFromEnd(fromArr(new int[]{1,2,3,4,5}), 2))); }
}
