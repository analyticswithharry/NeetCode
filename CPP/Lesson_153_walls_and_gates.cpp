// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 153 -- Walls And Gates
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 77
// =============================================================
//
// QUESTION:
//   Grid: -1 wall, 0 gate, INF empty. Fill each empty with distance to nearest gate.
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
const int INF=INT_MAX;
vector<vector<int>> walls(vector<vector<int>> g){if(g.empty())return g;int m=g.size(),n=g[0].size();queue<pair<int,int>> q;for(int i=0;i<m;i++)for(int j=0;j<n;j++)if(g[i][j]==0)q.push({i,j});int D[4][2]={{-1,0},{1,0},{0,-1},{0,1}};while(!q.empty()){auto [i,j]=q.front();q.pop();for(auto& d:D){int ni=i+d[0],nj=j+d[1];if(ni>=0&&nj>=0&&ni<m&&nj<n&&g[ni][nj]==INF){g[ni][nj]=g[i][j]+1;q.push({ni,nj});}}}return g;}
int main(){auto r=walls({{INF,-1,0,INF},{INF,INF,INF,-1},{INF,-1,INF,-1},{0,-1,INF,INF}});for(auto&row:r){for(int x:row)cout<<(x==INF?-9:x)<<" ";cout<<"\n";}}
