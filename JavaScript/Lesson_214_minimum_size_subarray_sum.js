// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 214 -- Minimum Size Subarray Sum
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 107
// =============================================================
//
// QUESTION:
//   Return the minimum length of a contiguous subarray whose sum is >= target. 0 if none.
// =============================================================
function minSubArrayLen(t,n){let l=0,s=0,ans=Infinity;for(let r=0;r<n.length;r++){s+=n[r];while(s>=t){ans=Math.min(ans,r-l+1);s-=n[l++];}}return ans===Infinity?0:ans;}
console.log(minSubArrayLen(7,[2,3,1,2,4,3]));console.log(minSubArrayLen(11,[1,1,1,1,1,1]));
