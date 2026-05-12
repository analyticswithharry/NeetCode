// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 227 -- LRU Cache
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 114
// =============================================================
//
// QUESTION:
//   Design LRU cache with O(1) get and put.
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
class LRU{int c;list<pair<int,int>> l;unordered_map<int,list<pair<int,int>>::iterator> m;public:LRU(int c):c(c){}int get(int k){if(!m.count(k))return -1;l.splice(l.begin(),l,m[k]);return m[k]->second;}void put(int k,int v){if(m.count(k)){m[k]->second=v;l.splice(l.begin(),l,m[k]);return;}l.push_front({k,v});m[k]=l.begin();if((int)l.size()>c){m.erase(l.back().first);l.pop_back();}}};
int main(){LRU c(2);c.put(1,1);c.put(2,2);cout<<c.get(1)<<"\n";c.put(3,3);cout<<c.get(2)<<"\n";}
