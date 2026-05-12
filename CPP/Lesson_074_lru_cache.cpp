// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 074 -- LRU Cache
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 37
// =============================================================
//
// QUESTION:
//   Design an LRU cache with O(1) get and put.
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
class LRUCache {
    int cap; list<pair<int,int>> dq; unordered_map<int, list<pair<int,int>>::iterator> m;
public:
    LRUCache(int c): cap(c) {}
    int get(int k){
        auto it = m.find(k); if (it == m.end()) return -1;
        dq.splice(dq.begin(), dq, it->second); return it->second->second;
    }
    void put(int k, int v){
        auto it = m.find(k);
        if (it != m.end()){ it->second->second = v; dq.splice(dq.begin(), dq, it->second); return; }
        dq.push_front({k,v}); m[k] = dq.begin();
        if ((int)dq.size() > cap){ m.erase(dq.back().first); dq.pop_back(); }
    }
};
int main(){ LRUCache c(2); c.put(1,1); c.put(2,2); cout<<c.get(1)<<endl;
    c.put(3,3); cout<<c.get(2)<<endl; c.put(4,4);
    cout<<c.get(1)<<" "<<c.get(3)<<" "<<c.get(4)<<endl; }
