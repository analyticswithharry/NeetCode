// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 145 -- Construct Quad Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 73
// =============================================================
//
// QUESTION:
//   Given an n x n grid of 0/1, build a quad tree representation. Return root.
// =============================================================
class QN{constructor(v,leaf,tl=null,tr=null,bl=null,br=null){this.val=v;this.isLeaf=leaf;this.tl=tl;this.tr=tr;this.bl=bl;this.br=br;}}
function build(g){function rec(r,c,n){let same=true;for(let i=r;i<r+n;i++)for(let j=c;j<c+n;j++)if(g[i][j]!==g[r][c])same=false;if(same)return new QN(g[r][c]===1,true);const h=n/2;return new QN(true,false,rec(r,c,h),rec(r,c+h,h),rec(r+h,c,h),rec(r+h,c+h,h));}return rec(0,0,g.length);}
function ser(n){if(n.isLeaf)return [+n.val];return ['#',...ser(n.tl),...ser(n.tr),...ser(n.bl),...ser(n.br)];}
console.log(ser(build([[0,1],[1,0]])));
