// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 061 -- Contains Duplicate
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 31
// =============================================================
//
// QUESTION:
//   Given an integer array nums, return true if any value appears at least twice.
//
//   Example: [1,2,3,1] -> true; [1,2,3,4] -> false
// =============================================================

import java.util.*;
public class Lesson061_ContainsDuplicate {
    public boolean containsDuplicate(int[] nums){
        Set<Integer> s = new HashSet<>();
        for (int n: nums) if (!s.add(n)) return true;
        return false;
    }
    public static void main(String[] a){
        Lesson061_ContainsDuplicate x = new Lesson061_ContainsDuplicate();
        System.out.println(x.containsDuplicate(new int[]{1,2,3,1}));
        System.out.println(x.containsDuplicate(new int[]{1,2,3,4}));
    }
}
