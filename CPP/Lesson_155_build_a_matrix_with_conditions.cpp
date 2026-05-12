// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 155 -- Build a Matrix With Conditions
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 78
// =============================================================
//
// QUESTION:
//   Given k rows/cols and conditions for row/col orderings, place 1..k so each appears once and conditions are satisfied. Return matrix or [].
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
vector<int> topo(int k,vector<vector<int>> conds){vector<vector<int>> adj(k+1);vector<int> ind(k+1,0);for(auto& c:conds){adj[c[0]].push_back(c[1]);ind[c[1]]++;}queue<int> q;for(int i=1;i<=k;i++)if(ind[i]==0)q.push(i);vector<int> o;while(!q.empty()){int x=q.front();q.pop();o.push_back(x);for(int y:adj[x])if(--ind[y]==0)q.push(y);}return (int)o.size()==k?o:vector<int>{};}
vector<vector<int>> build(int k,vector<vector<int>> rC,vector<vector<int>> cC){auto r=topo(k,rC),c=topo(k,cC);if(r.empty()||c.empty())return {};vector<int> pos(k+1);for(int i=0;i<k;i++)pos[c[i]]=i;vector<vector<int>> g(k,vector<int>(k,0));for(int i=0;i<k;i++)g[i][pos[r[i]]]=r[i];return g;}
int main(){auto m=build(3,{{1,2},{3,2}},{{2,1},{3,2}});for(auto&r:m){for(int x:r)cout<<x<<" ";cout<<"\n";}}
