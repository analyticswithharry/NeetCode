// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 141 -- Binary Tree Level Order Traversal
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 71
// =============================================================
//
// QUESTION:
//   Return level-order traversal of a binary tree (values grouped by level).
// =============================================================
import java.util.*;
public class Lesson141_BinaryTreeLevelOrderTraversal{
  static class TN{int val;TN left,right;TN(int v){val=v;}TN(int v,TN l,TN r){val=v;left=l;right=r;}}
  static List<List<Integer>> levels(TN root){List<List<Integer>> res=new ArrayList<>();if(root==null)return res;Queue<TN> q=new ArrayDeque<>();q.add(root);while(!q.isEmpty()){List<Integer> lvl=new ArrayList<>();int n=q.size();for(int i=0;i<n;i++){TN x=q.poll();lvl.add(x.val);if(x.left!=null)q.add(x.left);if(x.right!=null)q.add(x.right);}res.add(lvl);}return res;}
  public static void main(String[]x){TN r=new TN(3,new TN(9,null,null),new TN(20,new TN(15,null,null),new TN(7,null,null)));System.out.println(levels(r));}
}
