// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 131 -- Time Based Key Value Store
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 66
// =============================================================
//
// QUESTION:
//   Design TimeMap: set(k,v,t) and get(k,t) returns value with greatest timestamp <= t.
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
struct TimeMap{ unordered_map<string,vector<pair<int,string>>> m; void set(string k,string v,int t){m[k].push_back({t,v});} string get(string k,int t){auto it=m.find(k);if(it==m.end())return ""; auto& v=it->second; int lo=0,hi=v.size()-1,r=-1; while(lo<=hi){int mid=(lo+hi)/2; if(v[mid].first<=t){r=mid;lo=mid+1;} else hi=mid-1;} return r<0?"":v[r].second;}};
int main(){TimeMap tm; tm.set("foo","bar",1); cout<<tm.get("foo",1)<<"\n"<<tm.get("foo",3)<<"\n"; tm.set("foo","bar2",4); cout<<tm.get("foo",4)<<"\n"<<tm.get("foo",5)<<"\n";}
