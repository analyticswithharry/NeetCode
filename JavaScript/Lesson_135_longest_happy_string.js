// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 135 -- Longest Happy String
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 68
// =============================================================
//
// QUESTION:
//   Given a,b,c counts of letters, build the longest string with at most a 'a', b 'b', c 'c' such that no three consecutive letters are equal.
// =============================================================
function longest(a,b,c){const h=[];if(a)h.push([a,'a']);if(b)h.push([b,'b']);if(c)h.push([c,'c']);const out=[];const popMax=()=>{let mi=0;for(let i=1;i<h.length;i++)if(h[i][0]>h[mi][0])mi=i;return h.splice(mi,1)[0];};while(h.length){const [c1,ch1]=popMax();if(out.length>=2&&out[out.length-1]===ch1&&out[out.length-2]===ch1){if(!h.length)break;const [c2,ch2]=popMax();out.push(ch2);if(c2-1)h.push([c2-1,ch2]);h.push([c1,ch1]);}else{out.push(ch1);if(c1-1)h.push([c1-1,ch1]);}}return out.join("");}
console.log(longest(1,1,7));console.log(longest(7,1,0));
