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
#include <vector>
#include <string>
#include <iostream>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <numeric>
#include <functional>
#include <cmath>
using namespace std;
class LFU{int c=0,mn=0;unordered_map<int,pair<int,int>> kv;unordered_map<int,list<int>> f;unordered_map<int,list<int>::iterator> it;public:LFU(int c):c(c){}void bump(int k){int fr=kv[k].second;f[fr].erase(it[k]);if(f[fr].empty()&&mn==fr)mn++;f[fr+1].push_back(k);it[k]=prev(f[fr+1].end());kv[k].second++;}int get(int k){if(!kv.count(k))return -1;bump(k);return kv[k].first;}void put(int k,int v){if(c==0)return;if(kv.count(k)){kv[k].first=v;bump(k);return;}if((int)kv.size()>=c){int ek=f[mn].front();f[mn].pop_front();kv.erase(ek);it.erase(ek);}kv[k]={v,1};f[1].push_back(k);it[k]=prev(f[1].end());mn=1;}};
int main(){LFU c(2);c.put(1,1);c.put(2,2);cout<<c.get(1)<<"\n";c.put(3,3);cout<<c.get(2)<<"\n";}
