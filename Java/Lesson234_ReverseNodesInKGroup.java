// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 234 -- Reverse Nodes In K Group
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 117
// =============================================================
//
// QUESTION:
//   Reverse nodes in groups of k. Remaining tail stays.
// =============================================================
public class Lesson234_ReverseNodesInKGroup{
  static class N{int v;N n;N(int v){this.v=v;}}
  static N reverseK(N head,int k){N d=new N(0);d.n=head;N g=d;while(true){N kth=g;for(int i=0;i<k;i++){kth=kth.n;if(kth==null)return d.n;}N nxt=kth.n,pre=nxt,cur=g.n;while(cur!=nxt){N t=cur.n;cur.n=pre;pre=cur;cur=t;}N tmp=g.n;g.n=kth;g=tmp;}}
  static N to(int[] a){N d=new N(0),c=d;for(int x:a){c.n=new N(x);c=c.n;}return d.n;}
  public static void main(String[]a){N r=reverseK(to(new int[]{1,2,3,4,5}),2);while(r!=null){System.out.print(r.v+" ");r=r.n;}System.out.println();}
}
