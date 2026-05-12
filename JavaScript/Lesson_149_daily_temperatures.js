// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 149 -- Daily Temperatures
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 75
// =============================================================
//
// QUESTION:
//   For each day, return number of days until a warmer temperature, or 0.
// =============================================================
function dailyT(t){const r=new Array(t.length).fill(0);const st=[];for(let i=0;i<t.length;i++){while(st.length&&t[st[st.length-1]]<t[i]){const j=st.pop();r[j]=i-j;}st.push(i);}return r;}
console.log(dailyT([73,74,75,71,69,72,76,73]));
