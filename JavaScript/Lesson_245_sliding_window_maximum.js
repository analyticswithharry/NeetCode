// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 245 -- Sliding Window Maximum
// Category   : Sliding Window
// Difficulty : Hard
// Study Plan : Day 123
// =============================================================
//
// QUESTION:
//   Max in each window of size k. Monotonic deque.
// =============================================================
function maxSliding(n,k){const dq=[],out=[];for(let i=0;i<n.length;i++){while(dq.length&&n[dq[dq.length-1]]<=n[i])dq.pop();dq.push(i);if(dq[0]<=i-k)dq.shift();if(i>=k-1)out.push(n[dq[0]]);}return out;}
console.log(maxSliding([1,3,-1,-3,5,3,6,7],3));
