// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 139 -- Roman to Integer
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 70
// =============================================================
//
// QUESTION:
//   Convert Roman numeral string to integer.
// =============================================================
import java.util.*;
public class Lesson139_RomanToInteger{
  static int r2i(String s){Map<Character,Integer> m=Map.of('I',1,'V',5,'X',10,'L',50,'C',100,'D',500,'M',1000);int t=0,p=0;for(int i=s.length()-1;i>=0;i--){int v=m.get(s.charAt(i));if(v<p)t-=v;else{t+=v;p=v;}}return t;}
  public static void main(String[]x){System.out.println(r2i("III"));System.out.println(r2i("LVIII"));System.out.println(r2i("MCMXCIV"));}
}
