// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 118 -- Meeting Rooms III
// Category   : Intervals
// Difficulty : Hard
// Study Plan : Day 59
// =============================================================
//
// QUESTION:
//   Given n rooms (0..n-1) and meetings [start,end], assign meetings to lowest-numbered available room, delaying if needed (preserving duration). Return room hosting most meetings.
// =============================================================
function mostBooked(n,meets){meets.sort((a,b)=>a[0]-b[0]);const free=Array.from({length:n},(_,i)=>i);const busy=[];const cnt=new Array(n).fill(0);const popMin=arr=>{let mi=0;for(let i=1;i<arr.length;i++)if(Array.isArray(arr[i])?(arr[i][0]<arr[mi][0]||(arr[i][0]===arr[mi][0]&&arr[i][1]<arr[mi][1])):arr[i]<arr[mi])mi=i;return arr.splice(mi,1)[0];};for(const [s,e] of meets){for(let i=busy.length-1;i>=0;i--)if(busy[i][0]<=s){free.push(busy[i][1]);busy.splice(i,1);}if(free.length){const r=popMin(free);busy.push([e,r]);cnt[r]++;}else{const [t,r]=popMin(busy);busy.push([t+e-s,r]);cnt[r]++;}}let mi=0;for(let i=1;i<n;i++)if(cnt[i]>cnt[mi])mi=i;return mi;}
console.log(mostBooked(2,[[0,10],[1,5],[2,7],[3,4]]));
