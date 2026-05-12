// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 140 -- Set Matrix Zeroes
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 70
// =============================================================
//
// QUESTION:
//   Given m x n matrix, if an element is 0, set its entire row and column to 0. In place.
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
vector<vector<int>> setZero(vector<vector<int>> g){int m=g.size(),n=g[0].size();bool r0=false,c0=false;for(int j=0;j<n;j++)if(g[0][j]==0)r0=true;for(int i=0;i<m;i++)if(g[i][0]==0)c0=true;for(int i=1;i<m;i++)for(int j=1;j<n;j++)if(g[i][j]==0){g[i][0]=0;g[0][j]=0;}for(int i=1;i<m;i++)for(int j=1;j<n;j++)if(g[i][0]==0||g[0][j]==0)g[i][j]=0;if(r0)for(int j=0;j<n;j++)g[0][j]=0;if(c0)for(int i=0;i<m;i++)g[i][0]=0;return g;}
int main(){auto r=setZero({{1,1,1},{1,0,1},{1,1,1}});for(auto&row:r){for(int x:row)cout<<x<<" ";cout<<"\n";}}
