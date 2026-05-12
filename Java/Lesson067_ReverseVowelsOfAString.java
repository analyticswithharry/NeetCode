// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 067 -- Reverse Vowels of a String
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 34
// =============================================================
//
// QUESTION:
//   Reverse only the vowels of a string. Vowels: a,e,i,o,u (and uppercase).
//
//   Example: hello -> holle
// =============================================================

public class Lesson067_ReverseVowelsOfAString {
    public String reverseVowels(String s){
        char[] a = s.toCharArray(); String v = "aeiouAEIOU"; int l=0,r=a.length-1;
        while (l<r){ while (l<r && v.indexOf(a[l])<0) l++; while (l<r && v.indexOf(a[r])<0) r--;
            char t=a[l]; a[l]=a[r]; a[r]=t; l++; r--; }
        return new String(a);
    }
    public static void main(String[] x){
        System.out.println(new Lesson067_ReverseVowelsOfAString().reverseVowels("hello"));
        System.out.println(new Lesson067_ReverseVowelsOfAString().reverseVowels("leetcode"));
    }
}
