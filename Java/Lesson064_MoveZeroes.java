// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 064 -- Move Zeroes
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 32
// =============================================================
//
// QUESTION:
//   Move all 0s to the end while maintaining relative order. In-place.
//
//   Example: [0,1,0,3,12] -> [1,3,12,0,0]
// =============================================================

import java.util.*;
public class Lesson064_MoveZeroes {
    public int[] moveZeroes(int[] nums){
        int j=0;
        for (int i=0;i<nums.length;i++) if (nums[i]!=0){ int t=nums[i]; nums[i]=nums[j]; nums[j]=t; j++; }
        return nums;
    }
    public static void main(String[] a){ System.out.println(Arrays.toString(new Lesson064_MoveZeroes().moveZeroes(new int[]{0,1,0,3,12}))); }
}
