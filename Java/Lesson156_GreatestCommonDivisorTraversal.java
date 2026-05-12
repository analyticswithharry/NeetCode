// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 156 -- Greatest Common Divisor Traversal
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 78
// =============================================================
//
// QUESTION:
//   You can move between indices i,j if gcd(nums[i],nums[j])>1. Return true iff every pair is connected.
// =============================================================
import java.util.*;
public class Lesson156_GreatestCommonDivisorTraversal{
  static int[] par;
  static int f(int x){while(par[x]!=x){par[x]=par[par[x]];x=par[x];}return x;}
  static void u(int x,int y){x=f(x);y=f(y);if(x!=y)par[x]=y;}
  static List<Integer> primes(int x){List<Integer> r=new ArrayList<>();for(int d=2;1L*d*d<=x;d++)if(x%d==0){r.add(d);while(x%d==0)x/=d;}if(x>1)r.add(x);return r;}
  static boolean can(int[]a){int n=a.length;par=new int[n];for(int i=0;i<n;i++)par[i]=i;Map<Integer,Integer> pm=new HashMap<>();for(int i=0;i<n;i++)for(int p:primes(a[i])){if(pm.containsKey(p))u(i,pm.get(p));else pm.put(p,i);}int r=f(0);for(int i=0;i<n;i++)if(f(i)!=r)return false;return true;}
  public static void main(String[]x){System.out.println(can(new int[]{2,3,6}));System.out.println(can(new int[]{3,9,5}));System.out.println(can(new int[]{4,3,12,8}));}
}
