// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 159 -- Find Median From Data Stream
// Category   : Heap Priority Queue
// Difficulty : Hard
// Study Plan : Day 80
// =============================================================
//
// QUESTION:
//   Design MedianFinder: addNum, findMedian.
// =============================================================
class MedianFinder{constructor(){this.lo=[];this.hi=[];}_pushMax(h,x){h.push(x);let i=h.length-1;while(i>0){const p=(i-1)>>1;if(h[p]<h[i]){[h[p],h[i]]=[h[i],h[p]];i=p;}else break;}}_popMax(h){const t=h[0],l=h.pop();if(h.length){h[0]=l;let i=0;for(;;){const a=2*i+1,b=a+1;let m=i;if(a<h.length&&h[a]>h[m])m=a;if(b<h.length&&h[b]>h[m])m=b;if(m===i)break;[h[i],h[m]]=[h[m],h[i]];i=m;}}return t;}_pushMin(h,x){h.push(x);let i=h.length-1;while(i>0){const p=(i-1)>>1;if(h[p]>h[i]){[h[p],h[i]]=[h[i],h[p]];i=p;}else break;}}_popMin(h){const t=h[0],l=h.pop();if(h.length){h[0]=l;let i=0;for(;;){const a=2*i+1,b=a+1;let m=i;if(a<h.length&&h[a]<h[m])m=a;if(b<h.length&&h[b]<h[m])m=b;if(m===i)break;[h[i],h[m]]=[h[m],h[i]];i=m;}}return t;}addNum(x){this._pushMax(this.lo,x);this._pushMin(this.hi,this._popMax(this.lo));if(this.hi.length>this.lo.length)this._pushMax(this.lo,this._popMin(this.hi));}findMedian(){if(this.lo.length>this.hi.length)return this.lo[0];return (this.lo[0]+this.hi[0])/2;}}
const m=new MedianFinder();for(const x of [1,2,3]){m.addNum(x);console.log(m.findMedian());}
