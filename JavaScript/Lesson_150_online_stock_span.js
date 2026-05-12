// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 150 -- Online Stock Span
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 75
// =============================================================
//
// QUESTION:
//   Implement StockSpanner.next(price): consecutive days <= today's price (including today).
// =============================================================
class StockSpanner{constructor(){this.st=[];}next(p){let s=1;while(this.st.length&&this.st[this.st.length-1][0]<=p)s+=this.st.pop()[1];this.st.push([p,s]);return s;}}
const s=new StockSpanner();
console.log([100,80,60,70,60,75,85].map(x=>s.next(x)));
