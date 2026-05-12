// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 160 -- IPO
// Category   : Heap Priority Queue
// Difficulty : Hard
// Study Plan : Day 80
// =============================================================
//
// QUESTION:
//   Pick at most k projects with capital >= w each. Each project gives profit; w grows. Maximize final w.
// =============================================================
function ipo(k,w,profits,capital){const proj=capital.map((c,i)=>[c,profits[i]]).sort((a,b)=>a[0]-b[0]);const h=[];let i=0;const popMax=()=>{let mi=0;for(let j=1;j<h.length;j++)if(h[j]>h[mi])mi=j;return h.splice(mi,1)[0];};for(let s=0;s<k;s++){while(i<proj.length&&proj[i][0]<=w)h.push(proj[i++][1]);if(!h.length)break;w+=popMax();}return w;}
console.log(ipo(2,0,[1,2,3],[0,1,1]));console.log(ipo(3,0,[1,2,3],[0,1,2]));
