// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 122 -- Asteroid Collision
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 61
// =============================================================
//
// QUESTION:
//   Given an array of asteroids (positive=right, negative=left), return state after all collisions.
// =============================================================
function collide(a){const st=[];outer: for(const x of a){while(st.length&&x<0&&st[st.length-1]>0){if(st[st.length-1]<-x){st.pop();continue;}else if(st[st.length-1]===-x){st.pop();}continue outer;}st.push(x);}return st;}
console.log(collide([5,10,-5]));console.log(collide([8,-8]));console.log(collide([10,2,-5]));
