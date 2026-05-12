// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 212 -- Accounts Merge
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 106
// =============================================================
//
// QUESTION:
//   Merge accounts that share any common email. Return merged accounts with name + sorted unique emails.
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
unordered_map<string,string> p,own;
string f(string x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
int main(){vector<vector<string>> acc={{"A","a@x","b@x"},{"A","b@x","c@x"},{"B","d@x"}};for(auto& a:acc){for(int i=1;i<(int)a.size();i++){if(!p.count(a[i]))p[a[i]]=a[i];own[a[i]]=a[0];p[f(a[i])]=f(a[1]);}}map<string,vector<string>> g;for(auto&[k,_]:p)g[f(k)].push_back(k);for(auto&[r,v]:g){sort(v.begin(),v.end());cout<<own[v[0]];for(auto&e:v)cout<<","<<e;cout<<"\n";}}
