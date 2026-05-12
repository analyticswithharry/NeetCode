// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 072 -- Linked List Cycle
// Category   : Linked List
// Difficulty : Easy
// Study Plan : Day 36
// =============================================================
//
// QUESTION:
//   Determine if a linked list has a cycle. Floyd's tortoise and hare.
// =============================================================

public class Lesson072_LinkedListCycle {
    static class ListNode { int val; ListNode next; ListNode(int v){val=v;} }
    public boolean hasCycle(ListNode head){
        ListNode slow=head, fast=head;
        while (fast!=null && fast.next!=null){ slow=slow.next; fast=fast.next.next; if (slow==fast) return true; }
        return false;
    }
    public static void main(String[] a){
        ListNode x=new ListNode(1), y=new ListNode(2), z=new ListNode(3);
        x.next=y; y.next=z; z.next=x; System.out.println(new Lesson072_LinkedListCycle().hasCycle(x));
        ListNode p=new ListNode(1); p.next=new ListNode(2); System.out.println(new Lesson072_LinkedListCycle().hasCycle(p));
    }
}
