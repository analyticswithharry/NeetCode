// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 220 -- Minimum Window Substring
// Category   : Sliding Window
// Difficulty : Hard
// Study Plan : Day 110
// =============================================================
//
// QUESTION:
//   Smallest substring of s containing all chars of t.
// =============================================================
function minWindow(s,t){if(!t)return"";const need={};for(const c of t)need[c]=(need[c]||0)+1;const have={};let nn=Object.keys(need).length,hn=0,res=[-1,-1],rl=Infinity,l=0;for(let r=0;r<s.length;r++){const c=s[r];have[c]=(have[c]||0)+1;if(c in need&&have[c]===need[c])hn++;while(hn===nn){if(r-l+1<rl){res=[l,r];rl=r-l+1;}have[s[l]]--;if(s[l] in need&&have[s[l]]<need[s[l]])hn--;l++;}}return rl===Infinity?"":s.slice(res[0],res[1]+1);}
console.log(minWindow("ADOBECODEBANC","ABC"));
