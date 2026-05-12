// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 069 -- Add Two Numbers
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 35
// =============================================================
//
// QUESTION:
//   Two non-empty linked lists representing non-negative integers in reverse order. Return sum as linked list.
//
//   Example: 2->4->3 + 5->6->4 = 7->0->8 (i.e., 342 + 465 = 807)
// =============================================================

import java.util.*;
public class Lesson069_AddTwoNumbers {
    static class ListNode { int val; ListNode next; ListNode(int v){val=v;} }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2){
        ListNode dummy = new ListNode(0), cur = dummy; int carry = 0;
        while (l1!=null || l2!=null || carry>0){
            int x = (l1!=null?l1.val:0) + (l2!=null?l2.val:0) + carry;
            carry = x/10; cur.next = new ListNode(x%10); cur = cur.next;
            if (l1!=null) l1 = l1.next; if (l2!=null) l2 = l2.next;
        }
        return dummy.next;
    }
    static ListNode fromArr(int[] a){ ListNode d=new ListNode(0), c=d; for (int x: a){ c.next=new ListNode(x); c=c.next; } return d.next; }
    static List<Integer> toArr(ListNode n){ List<Integer> r=new ArrayList<>(); while (n!=null){ r.add(n.val); n=n.next; } return r; }
    public static void main(String[] a){
        System.out.println(toArr(new Lesson069_AddTwoNumbers().addTwoNumbers(fromArr(new int[]{2,4,3}), fromArr(new int[]{5,6,4}))));
    }
}
