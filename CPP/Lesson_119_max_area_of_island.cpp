// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 119 -- Max Area of Island
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 60
// =============================================================
//
// QUESTION:
//   Given m x n binary grid, return max area of an island (4-directionally connected 1s).
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
int M,N; vector<vector<int>>* G;
int dfs(int i,int j){if(i<0||j<0||i>=M||j>=N||(*G)[i][j]!=1)return 0;(*G)[i][j]=0;return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1);}
int maxArea(vector<vector<int>> g){G=&g;M=g.size();N=g[0].size();int b=0;for(int i=0;i<M;i++)for(int j=0;j<N;j++)if(g[i][j]==1)b=max(b,dfs(i,j));return b;}
int main(){cout<<maxArea({{1,1,0},{1,0,0},{0,0,1}})<<"\n";}
