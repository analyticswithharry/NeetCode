// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 216 -- Partition Labels
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 108
// =============================================================
//
// QUESTION:
//   Partition string so each char appears in at most one part. Return sizes.
// =============================================================
function partitionLabels(s){const last={};for(let i=0;i<s.length;i++)last[s[i]]=i;const r=[];let st=0,e=0;for(let i=0;i<s.length;i++){e=Math.max(e,last[s[i]]);if(i===e){r.push(e-st+1);st=i+1;}}return r;}
console.log(partitionLabels("ababcbacadefegdehijhklij"));
