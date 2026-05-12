// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 249 -- Serialize And Deserialize Binary Tree
// Category   : Trees
// Difficulty : Hard
// Study Plan : Day 125
// =============================================================
//
// QUESTION:
//   Pre-order serialize with null markers; queue-based deserialize.
// =============================================================
class T{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function ser(r){const out=[];const dfs=n=>{if(!n){out.push("#");return;}out.push(n.v);dfs(n.l);dfs(n.r);};dfs(r);return out.join(",");}
function des(s){const arr=s.split(",");let i=0;const dfs=()=>{const x=arr[i++];if(x==="#")return null;const n=new T(+x);n.l=dfs();n.r=dfs();return n;};return dfs();}
const r=new T(1,new T(2),new T(3,new T(4),new T(5)));const s=ser(r);console.log(s);console.log(ser(des(s)));
