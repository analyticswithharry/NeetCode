// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 117 -- Meeting Rooms II
// Category   : Intervals
// Difficulty : Medium
// Study Plan : Day 59
// =============================================================
//
// QUESTION:
//   Given an array of meeting time intervals, return the minimum number of conference rooms required.
// =============================================================
function minRooms(it){it.sort((a,b)=>a[0]-b[0]);const h=[];for(const [s,e] of it){let mi=0;for(let i=1;i<h.length;i++)if(h[i]<h[mi])mi=i;if(h.length&&h[mi]<=s)h.splice(mi,1);h.push(e);}return h.length;}
console.log(minRooms([[0,30],[5,10],[15,20]]));
console.log(minRooms([[7,10],[2,4]]));
