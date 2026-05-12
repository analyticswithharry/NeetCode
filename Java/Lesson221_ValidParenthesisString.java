// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 221 -- Valid Parenthesis String
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 111
// =============================================================
//
// QUESTION:
//   '*' can be '(' ')' or empty. Determine if string can be valid.
// =============================================================
public class Lesson221_ValidParenthesisString{
  static boolean checkValid(String s){int lo=0,hi=0;for(char c:s.toCharArray()){lo+=c=='('?1:-1;hi+=c!=')'?1:-1;if(hi<0)return false;if(lo<0)lo=0;}return lo==0;}
  public static void main(String[]a){System.out.println(checkValid("(*))"));}
}
