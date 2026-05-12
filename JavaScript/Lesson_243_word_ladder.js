// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 243 -- Word Ladder
// Category   : Graphs
// Difficulty : Hard
// Study Plan : Day 122
// =============================================================
//
// QUESTION:
//   Shortest transformation sequence length from begin to end. BFS with wildcard buckets.
// =============================================================
function ladderLength(b,e,wl){const ws=new Set(wl);if(!ws.has(e))return 0;const L=b.length;const buc={};for(const w of ws)for(let i=0;i<L;i++){const k=w.slice(0,i)+'*'+w.slice(i+1);(buc[k]=buc[k]||[]).push(w);}const q=[[b,1]];const seen=new Set([b]);while(q.length){const [w,d]=q.shift();if(w===e)return d;for(let i=0;i<L;i++){const k=w.slice(0,i)+'*'+w.slice(i+1);for(const n of (buc[k]||[]))if(!seen.has(n)){seen.add(n);q.push([n,d+1]);}}}return 0;}
console.log(ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]));
