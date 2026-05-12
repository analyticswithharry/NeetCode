// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 003 -- Reverse Linked List
// Category   : Linked List
// Difficulty : Easy
// Study Plan : Day 2
// =============================================================
//
// QUESTION:
//   Given the head of a singly linked list, reverse the list and return
//   the new head.
//
//   Example:
//     Input : 1 -> 2 -> 3 -> 4 -> 5
//     Output: 5 -> 4 -> 3 -> 2 -> 1
// =============================================================

import java.util.*;

public class Lesson003_ReverseLinkedList {
    static class ListNode { int val; ListNode next; ListNode(int v){val=v;} }

    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        while (head != null) { ListNode n = head.next; head.next = prev; prev = head; head = n; }
        return prev;
    }

    public static void main(String[] args) {
        ListNode h = new ListNode(1); h.next = new ListNode(2); h.next.next = new ListNode(3);
        h.next.next.next = new ListNode(4); h.next.next.next.next = new ListNode(5);
        ListNode r = new Lesson003_ReverseLinkedList().reverseList(h);
        List<Integer> out = new ArrayList<>();
        while (r != null) { out.add(r.val); r = r.next; }
        System.out.println(out);
    }
}
