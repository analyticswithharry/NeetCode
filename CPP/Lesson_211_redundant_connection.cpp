// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 211 -- Redundant Connection
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 106
// =============================================================
//
// QUESTION:
//   Given an n-node tree with one extra edge (forming exactly one cycle), return the edge that can be removed.
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
vector<int> p;
int f(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
vector<int> findRedundant(vector<vector<int>> e){p.assign(e.size()+1,0);iota(p.begin(),p.end(),0);for(auto& x:e){int ra=f(x[0]),rb=f(x[1]);if(ra==rb)return x;p[ra]=rb;}return {};}
int main(){auto r=findRedundant({{1,2},{1,3},{2,3}});cout<<r[0]<<","<<r[1]<<"\n";}
