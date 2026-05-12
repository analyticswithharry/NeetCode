// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 063 -- Encode and Decode Strings
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 32
// =============================================================
//
// QUESTION:
//   Design encode/decode of a list of strings into one string and back.
//
//   Strategy: prefix each string with its length and a delimiter (e.g., 5#hello).
// =============================================================

import java.util.*;
public class Lesson063_EncodeAndDecodeStrings {
    public String encode(List<String> strs){
        StringBuilder sb = new StringBuilder();
        for (String s: strs) sb.append(s.length()).append('#').append(s);
        return sb.toString();
    }
    public List<String> decode(String s){
        List<String> out = new ArrayList<>(); int i=0;
        while (i < s.length()){ int j = s.indexOf('#', i); int n = Integer.parseInt(s.substring(i,j));
            out.add(s.substring(j+1, j+1+n)); i = j+1+n; }
        return out;
    }
    public static void main(String[] a){
        Lesson063_EncodeAndDecodeStrings c = new Lesson063_EncodeAndDecodeStrings();
        String e = c.encode(Arrays.asList("lint","code","love","you"));
        System.out.println(e); System.out.println(c.decode(e));
    }
}
