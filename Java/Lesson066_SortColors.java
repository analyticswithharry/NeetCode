// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 066 -- Sort Colors
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 33
// =============================================================
//
// QUESTION:
//   Sort an array containing only 0,1,2 in-place. Dutch National Flag.
//
//   Example: [2,0,2,1,1,0] -> [0,0,1,1,2,2]
// =============================================================

import java.util.*;
public class Lesson066_SortColors {
    public int[] sortColors(int[] nums){
        int l=0,m=0,r=nums.length-1;
        while (m<=r){
            if (nums[m]==0){ int t=nums[l]; nums[l]=nums[m]; nums[m]=t; l++; m++; }
            else if (nums[m]==2){ int t=nums[m]; nums[m]=nums[r]; nums[r]=t; r--; }
            else m++;
        }
        return nums;
    }
    public static void main(String[] a){ System.out.println(Arrays.toString(new Lesson066_SortColors().sortColors(new int[]{2,0,2,1,1,0}))); }
}
