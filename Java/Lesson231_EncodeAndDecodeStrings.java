// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 231 -- Encode and Decode Strings
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 116
// =============================================================
//
// QUESTION:
//   Length-prefix encoding for arbitrary strings.
// =============================================================
import java.util.*;
public class Lesson231_EncodeAndDecodeStrings{
  static String encode(List<String> a){StringBuilder sb=new StringBuilder();for(String s:a)sb.append(s.length()).append('#').append(s);return sb.toString();}
  static List<String> decode(String s){List<String> r=new ArrayList<>();int i=0;while(i<s.length()){int j=s.indexOf('#',i);int n=Integer.parseInt(s.substring(i,j));r.add(s.substring(j+1,j+1+n));i=j+1+n;}return r;}
  public static void main(String[]a){String e=encode(Arrays.asList("hello","world","#42"));System.out.println(e);System.out.println(decode(e));}
}
