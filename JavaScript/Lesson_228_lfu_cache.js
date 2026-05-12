// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 228 -- LFU Cache
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 114
// =============================================================
//
// QUESTION:
//   LFU eviction; tie-break by least recently used. Use freq buckets of OrderedDict.
// =============================================================
class LFU{constructor(c){this.c=c;this.k=new Map();this.f=new Map();this.mn=0;}_bucket(f){if(!this.f.has(f))this.f.set(f,new Map());return this.f.get(f);}_bump(k){const [v,f]=this.k.get(k);this._bucket(f).delete(k);if(this._bucket(f).size===0&&this.mn===f)this.mn++;this._bucket(f+1).set(k,v);this.k.set(k,[v,f+1]);}get(k){if(!this.k.has(k))return -1;this._bump(k);return this.k.get(k)[0];}put(k,v){if(this.c===0)return;if(this.k.has(k)){this.k.set(k,[v,this.k.get(k)[1]]);this._bucket(this.k.get(k)[1]).set(k,v);this._bump(k);return;}if(this.k.size>=this.c){const b=this._bucket(this.mn);const ek=b.keys().next().value;b.delete(ek);this.k.delete(ek);}this.k.set(k,[v,1]);this._bucket(1).set(k,v);this.mn=1;}}
const c=new LFU(2);c.put(1,1);c.put(2,2);console.log(c.get(1));c.put(3,3);console.log(c.get(2));
