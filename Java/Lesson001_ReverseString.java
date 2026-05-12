// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 001 -- Reverse String
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 1
// =============================================================
//
// QUESTION:
//   Write a function that reverses a string. The input string is given as
//   an array of characters s. You must do this by modifying the input array
//   in-place with O(1) extra memory.
//
//   Example:
//     Input : s = ['h','e','l','l','o']
//     Output: ['o','l','l','e','h']
// =============================================================

import java.util.Arrays;

public class Lesson001_ReverseString {
    public void reverseString(char[] s) {
        int l = 0, r = s.length - 1;
        while (l < r) { char t = s[l]; s[l++] = s[r]; s[r--] = t; }
    }
    public static void main(String[] args) {
        char[] s = {'h','e','l','l','o'};
        new Lesson001_ReverseString().reverseString(s);
        System.out.println(Arrays.toString(s));
    }
}
