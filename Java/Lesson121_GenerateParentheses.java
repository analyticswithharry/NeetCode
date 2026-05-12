// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 121 -- Generate Parentheses
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 61
// =============================================================
//
// QUESTION:
//   Given n pairs of parentheses, generate all combinations of well-formed parentheses.
// =============================================================
import java.util.*;
public class Lesson121_GenerateParentheses{
  static List<String> R=new ArrayList<>(); static int N;
  static void rec(String s,int o,int c){if(s.length()==2*N){R.add(s);return;}if(o<N)rec(s+"(",o+1,c);if(c<o)rec(s+")",o,c+1);}
  static List<String> gen(int n){R.clear();N=n;rec("",0,0);return R;}
  public static void main(String[]x){System.out.println(gen(3));}
}
