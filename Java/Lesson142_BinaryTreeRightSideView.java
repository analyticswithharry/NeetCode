// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 142 -- Binary Tree Right Side View
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 71
// =============================================================
//
// QUESTION:
//   Return values seen from the right side of a binary tree.
// =============================================================
import java.util.*;
public class Lesson142_BinaryTreeRightSideView{
  static class TN{int val;TN left,right;TN(int v){val=v;}TN(int v,TN l,TN r){val=v;left=l;right=r;}}
  static List<Integer> view(TN root){List<Integer> res=new ArrayList<>();if(root==null)return res;Queue<TN> q=new ArrayDeque<>();q.add(root);while(!q.isEmpty()){int n=q.size();for(int i=0;i<n;i++){TN x=q.poll();if(i==n-1)res.add(x.val);if(x.left!=null)q.add(x.left);if(x.right!=null)q.add(x.right);}}return res;}
  public static void main(String[]x){TN r=new TN(1,new TN(2,null,new TN(5,null,null)),new TN(3,null,new TN(4,null,null)));System.out.println(view(r));}
}
