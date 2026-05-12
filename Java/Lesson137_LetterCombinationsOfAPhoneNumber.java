// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 137 -- Letter Combinations of a Phone Number
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 69
// =============================================================
//
// QUESTION:
//   Given digits 2-9, return all possible letter combinations the number could represent.
// =============================================================
import java.util.*;
public class Lesson137_LetterCombinationsOfAPhoneNumber{
  static List<String> letters(String d){if(d.isEmpty())return new ArrayList<>();String[] m={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};List<String> r=new ArrayList<>();r.add("");for(char c:d.toCharArray()){List<String> n=new ArrayList<>();for(String p:r)for(char x:m[c-'0'].toCharArray())n.add(p+x);r=n;}return r;}
  public static void main(String[]x){System.out.println(letters("23"));}
}
