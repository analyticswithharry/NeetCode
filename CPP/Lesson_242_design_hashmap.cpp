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
class HM{int B=997;vector<vector<pair<int,int>>> b;public:HM(){b.assign(B,{});}int h(int k){return ((k%B)+B)%B;}void put(int k,int v){auto& x=b[h(k)];for(auto& p:x)if(p.first==k){p.second=v;return;}x.push_back({k,v});}int get(int k){for(auto& p:b[h(k)])if(p.first==k)return p.second;return -1;}void remove(int k){auto& x=b[h(k)];for(auto it=x.begin();it!=x.end();++it)if(it->first==k){x.erase(it);return;}}};
int main(){HM m;m.put(1,1);m.put(2,2);cout<<m.get(1)<<" "<<m.get(3)<<"\n";m.remove(1);cout<<m.get(1)<<"\n";}
