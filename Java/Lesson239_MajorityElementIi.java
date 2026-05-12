// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 239 -- Majority Element II
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 120
// =============================================================
//
// QUESTION:
//   All elements appearing more than n/3 times. Boyer-Moore variant.
// =============================================================
import java.util.*;
public class Lesson239_MajorityElementIi{
  static List<Integer> majorityIII(int[] nums){int c1=0,c2=0,n1=0,n2=1;for(int x:nums){if(x==n1)c1++;else if(x==n2)c2++;else if(c1==0){n1=x;c1=1;}else if(c2==0){n2=x;c2=1;}else{c1--;c2--;}}List<Integer> r=new ArrayList<>();for(int n:new int[]{n1,n2}){int cnt=0;for(int x:nums)if(x==n)cnt++;if(cnt>nums.length/3&&!r.contains(n))r.add(n);}return r;}
  public static void main(String[]a){System.out.println(majorityIII(new int[]{1,1,1,3,3,2,2,2}));}
}
