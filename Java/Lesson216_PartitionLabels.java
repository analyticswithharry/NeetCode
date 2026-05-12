// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 216 -- Partition Labels
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 108
// =============================================================
//
// QUESTION:
//   Partition string so each char appears in at most one part. Return sizes.
// =============================================================
import java.util.*;
public class Lesson216_PartitionLabels{
  static List<Integer> partitionLabels(String s){int[] last=new int[26];for(int i=0;i<s.length();i++)last[s.charAt(i)-'a']=i;List<Integer> r=new ArrayList<>();int st=0,e=0;for(int i=0;i<s.length();i++){e=Math.max(e,last[s.charAt(i)-'a']);if(i==e){r.add(e-st+1);st=i+1;}}return r;}
  public static void main(String[]a){System.out.println(partitionLabels("ababcbacadefegdehijhklij"));}
}
