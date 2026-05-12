// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 246 -- Largest Rectangle In Histogram
// Category   : Stack
// Difficulty : Hard
// Study Plan : Day 123
// =============================================================
//
// QUESTION:
//   Max rectangular area in histogram. Monotonic stack.
// =============================================================
function largestRect(h){const st=[];let best=0;h=[...h,0];for(let i=0;i<h.length;i++){while(st.length&&h[st[st.length-1]]>h[i]){const top=st.pop();const w=st.length===0?i:i-st[st.length-1]-1;best=Math.max(best,h[top]*w);}st.push(i);}return best;}
console.log(largestRect([2,1,5,6,2,3]));
