// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 217 -- Evaluate Division
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 109
// =============================================================
//
// QUESTION:
//   Given equations a/b=value, answer queries x/y. Build weighted graph and DFS.
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
unordered_map<string,unordered_map<string,double>> g;
double dfs(string s,string t,unordered_set<string>& seen){if(!g.count(s)||!g.count(t))return -1;if(s==t)return 1;seen.insert(s);for(auto&[n,w]:g[s]){if(seen.count(n))continue;double r=dfs(n,t,seen);if(r!=-1)return w*r;}return -1;}
int main(){vector<pair<string,string>> eq={{"a","b"},{"b","c"}};vector<double> v={2,3};for(int i=0;i<(int)eq.size();i++){g[eq[i].first][eq[i].second]=v[i];g[eq[i].second][eq[i].first]=1/v[i];}unordered_set<string> s;cout<<dfs("a","c",s)<<"\n";s.clear();cout<<dfs("a","e",s)<<"\n";}
