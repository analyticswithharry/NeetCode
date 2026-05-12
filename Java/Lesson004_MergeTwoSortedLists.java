// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 004 -- Merge Two Sorted Lists
// Category   : Linked List
// Difficulty : Easy
// Study Plan : Day 2
// =============================================================
//
// QUESTION:
//   You are given the heads of two sorted linked lists list1 and list2.
//   Merge them into one sorted list and return its head.
//
//   Example:
//     Input : 1->2->4, 1->3->4
//     Output: 1->1->2->3->4->4
// =============================================================

import java.util.*;

public class Lesson004_MergeTwoSortedLists {
    static class ListNode { int val; ListNode next; ListNode(){} ListNode(int v){val=v;} }

    public ListNode mergeTwoLists(ListNode a, ListNode b) {
        ListNode d = new ListNode(), t = d;
        while (a != null && b != null) {
            if (a.val <= b.val) { t.next = a; a = a.next; }
            else { t.next = b; b = b.next; }
            t = t.next;
        }
        t.next = (a != null) ? a : b;
        return d.next;
    }

    static ListNode build(int[] v) { ListNode d = new ListNode(), t = d;
        for (int x : v) { t.next = new ListNode(x); t = t.next; } return d.next; }

    public static void main(String[] args) {
        ListNode r = new Lesson004_MergeTwoSortedLists().mergeTwoLists(build(new int[]{1,2,4}), build(new int[]{1,3,4}));
        List<Integer> out = new ArrayList<>();
        while (r != null) { out.add(r.val); r = r.next; }
        System.out.println(out);
    }
}
