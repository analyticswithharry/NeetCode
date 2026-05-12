// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 073 -- Copy List With Random Pointer
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 37
// =============================================================
//
// QUESTION:
//   Deep copy a linked list where each node has next and a random pointer that may point to any node or null.
// =============================================================

import java.util.*;
public class Lesson073_CopyListWithRandomPointer {
    static class Node { int val; Node next, random; Node(int v){val=v;} }
    public Node copyRandomList(Node head){
        if (head==null) return null;
        Map<Node,Node> m = new HashMap<>(); Node cur = head;
        while (cur!=null){ m.put(cur, new Node(cur.val)); cur = cur.next; }
        cur = head;
        while (cur!=null){ m.get(cur).next = m.get(cur.next); m.get(cur).random = m.get(cur.random); cur = cur.next; }
        return m.get(head);
    }
    public static void main(String[] a){
        Node x=new Node(1), y=new Node(2); x.next=y; x.random=y; y.random=y;
        Node c = new Lesson073_CopyListWithRandomPointer().copyRandomList(x);
        System.out.println(c.val+","+c.random.val+" "+c.next.val+","+c.next.random.val);
    }
}
