// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 232 -- Range Sum Query 2D Immutable
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 116
// =============================================================
//
// QUESTION:
//   Build prefix sum 2D for O(1) region queries.
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
struct NM{vector<vector<int>> p;NM(vector<vector<int>> m){int R=m.size(),C=m[0].size();p.assign(R+1,vector<int>(C+1,0));for(int i=0;i<R;i++)for(int j=0;j<C;j++)p[i+1][j+1]=m[i][j]+p[i][j+1]+p[i+1][j]-p[i][j];}int sumRegion(int r1,int c1,int r2,int c2){return p[r2+1][c2+1]-p[r1][c2+1]-p[r2+1][c1]+p[r1][c1];}};
int main(){NM n({{3,0,1},{5,6,3},{1,2,0}});cout<<n.sumRegion(0,0,2,2)<<"\n";cout<<n.sumRegion(1,1,2,2)<<"\n";}
