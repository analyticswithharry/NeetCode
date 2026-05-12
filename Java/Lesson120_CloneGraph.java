// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 120 -- Clone Graph
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 60
// =============================================================
//
// QUESTION:
//   Given a node in a connected undirected graph, return a deep copy of the graph.
// =============================================================
import java.util.*;
public class Lesson120_CloneGraph{
  static class Node{int val;List<Node> neighbors=new ArrayList<>();Node(int v){val=v;}}
  static Map<Node,Node> seen=new HashMap<>();
  static Node clone(Node n){if(n==null)return null;if(seen.containsKey(n))return seen.get(n);Node c=new Node(n.val);seen.put(n,c);for(Node y:n.neighbors)c.neighbors.add(clone(y));return c;}
  public static void main(String[]x){Node a=new Node(1),b=new Node(2);a.neighbors.add(b);b.neighbors.add(a);Node c=clone(a);System.out.println(c.val+" "+c.neighbors.get(0).val+" "+c.neighbors.get(0).neighbors.get(0).val);}
}
