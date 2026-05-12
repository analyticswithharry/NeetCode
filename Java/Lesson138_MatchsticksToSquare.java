// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 138 -- Matchsticks to Square
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 69
// =============================================================
//
// QUESTION:
//   Use all matchsticks to form a square. Return true if possible.
// =============================================================
import java.util.*;
public class Lesson138_MatchsticksToSquare{
  static int[] M; static int SIDE; static int[] S=new int[4];
  static boolean rec(int i){if(i==M.length)return S[0]==SIDE&&S[1]==SIDE&&S[2]==SIDE;for(int j=0;j<4;j++){if(S[j]+M[i]>SIDE)continue;if(j>0&&S[j]==S[j-1])continue;S[j]+=M[i];if(rec(i+1))return true;S[j]-=M[i];}return false;}
  static boolean square(int[]m){int s=0;for(int x:m)s+=x;if(s%4!=0)return false;SIDE=s/4;Arrays.sort(m);for(int i=0,j=m.length-1;i<j;i++,j--){int t=m[i];m[i]=m[j];m[j]=t;}if(m[0]>SIDE)return false;M=m;S=new int[4];return rec(0);}
  public static void main(String[]x){System.out.println(square(new int[]{1,1,2,2,2}));System.out.println(square(new int[]{3,3,3,3,4}));}
}
