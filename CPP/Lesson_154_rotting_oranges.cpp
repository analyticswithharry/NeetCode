// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 154 -- Rotting Oranges
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 77
// =============================================================
//
// QUESTION:
//   0 empty, 1 fresh, 2 rotten. Each minute rotten infects 4-neighbor fresh. Min minutes to rot all, or -1.
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
int rot(vector<vector<int>> g){int m=g.size(),n=g[0].size();queue<tuple<int,int,int>> q;int fresh=0;for(int i=0;i<m;i++)for(int j=0;j<n;j++){if(g[i][j]==2)q.push({i,j,0});else if(g[i][j]==1)fresh++;}int t=0,D[4][2]={{-1,0},{1,0},{0,-1},{0,1}};while(!q.empty()){auto [i,j,k]=q.front();q.pop();t=k;for(auto& d:D){int ni=i+d[0],nj=j+d[1];if(ni>=0&&nj>=0&&ni<m&&nj<n&&g[ni][nj]==1){g[ni][nj]=2;fresh--;q.push({ni,nj,k+1});}}}return fresh?-1:t;}
int main(){cout<<rot({{2,1,1},{1,1,0},{0,1,1}})<<"\n"<<rot({{2,1,1},{0,1,1},{1,0,1}})<<"\n";}
