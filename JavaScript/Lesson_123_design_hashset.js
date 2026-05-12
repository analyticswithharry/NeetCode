// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 123 -- Design HashSet
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 62
// =============================================================
//
// QUESTION:
//   Design a HashSet (without built-in set): add, remove, contains.
// =============================================================
class MyHashSet{constructor(){this.b=Array.from({length:769},()=>[]);}_h(k){return k%769;}add(k){const b=this.b[this._h(k)];if(!b.includes(k))b.push(k);}remove(k){const b=this.b[this._h(k)];const i=b.indexOf(k);if(i>=0)b.splice(i,1);}contains(k){return this.b[this._h(k)].includes(k);}}
const s=new MyHashSet();s.add(1);s.add(2);console.log(s.contains(1),s.contains(3));s.remove(2);console.log(s.contains(2));
