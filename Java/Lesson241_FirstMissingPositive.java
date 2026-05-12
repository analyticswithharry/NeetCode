// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 241 -- First Missing Positive
// Category   : Arrays and Hashing
// Difficulty : Hard
// Study Plan : Day 121
// =============================================================
//
// QUESTION:
//   Smallest missing positive int. O(n) time, O(1) extra space (cyclic placement).
// =============================================================
public class Lesson241_FirstMissingPositive{
  static int firstMissing(int[] n){int N=n.length;for(int i=0;i<N;i++)while(n[i]>=1&&n[i]<=N&&n[n[i]-1]!=n[i]){int j=n[i]-1;int t=n[i];n[i]=n[j];n[j]=t;}for(int i=0;i<N;i++)if(n[i]!=i+1)return i+1;return N+1;}
  public static void main(String[]a){System.out.println(firstMissing(new int[]{3,4,-1,1}));}
}
