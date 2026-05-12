// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 242 -- Design HashMap
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 121
// =============================================================
//
// QUESTION:
//   Implement HashMap with put/get/remove using bucket separate chaining.
// =============================================================
class HM{constructor(){this.B=997;this.b=Array.from({length:this.B},()=>[]);}_h(k){return ((k%this.B)+this.B)%this.B;}put(k,v){const b=this.b[this._h(k)];for(let i=0;i<b.length;i++)if(b[i][0]===k){b[i]=[k,v];return;}b.push([k,v]);}get(k){for(const [kk,vv] of this.b[this._h(k)])if(kk===k)return vv;return -1;}remove(k){const b=this.b[this._h(k)];for(let i=0;i<b.length;i++)if(b[i][0]===k){b.splice(i,1);return;}}}
const m=new HM();m.put(1,1);m.put(2,2);console.log(m.get(1),m.get(3));m.remove(1);console.log(m.get(1));
