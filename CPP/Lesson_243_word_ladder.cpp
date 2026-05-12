// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 243 -- Word Ladder
// Category   : Graphs
// Difficulty : Hard
// Study Plan : Day 122
// =============================================================
//
// QUESTION:
//   Shortest transformation sequence length from begin to end. BFS with wildcard buckets.
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
int ladderLength(string b,string e,vector<string> wl){unordered_set<string> ws(wl.begin(),wl.end());if(!ws.count(e))return 0;int L=b.size();unordered_map<string,vector<string>> buc;for(auto& w:ws)for(int i=0;i<L;i++){string k=w;k[i]='*';buc[k].push_back(w);}queue<pair<string,int>> q;q.push({b,1});unordered_set<string> seen={b};while(!q.empty()){auto [w,d]=q.front();q.pop();if(w==e)return d;for(int i=0;i<L;i++){string k=w;k[i]='*';for(auto& n:buc[k])if(!seen.count(n)){seen.insert(n);q.push({n,d+1});}}}return 0;}
int main(){cout<<ladderLength("hit","cog",{"hot","dot","dog","lot","log","cog"})<<"\n";}
