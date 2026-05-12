// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 218 -- Minimum Height Trees
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 109
// =============================================================
//
// QUESTION:
//   Given an undirected tree, find roots that produce minimum-height trees (peel leaves BFS).
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
vector<int> findMHT(int n,vector<vector<int>> e){if(n==1)return{0};vector<unordered_set<int>> g(n);vector<int> d(n);for(auto&x:e){g[x[0]].insert(x[1]);g[x[1]].insert(x[0]);d[x[0]]++;d[x[1]]++;}queue<int> q;for(int i=0;i<n;i++)if(d[i]==1)q.push(i);int rem=n;while(rem>2){int sz=q.size();rem-=sz;for(int i=0;i<sz;i++){int x=q.front();q.pop();for(int y:g[x]){d[y]--;if(d[y]==1)q.push(y);}}}vector<int> r;while(!q.empty()){r.push_back(q.front());q.pop();}return r;}
int main(){auto r=findMHT(6,{{3,0},{3,1},{3,2},{3,4},{5,4}});for(int x:r)cout<<x<<" ";cout<<"\n";}
