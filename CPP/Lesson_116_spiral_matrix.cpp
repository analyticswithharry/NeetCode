// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 116 -- Spiral Matrix
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 58
// =============================================================
//
// QUESTION:
//   Given m x n matrix, return all elements in spiral order.
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
vector<int> spiral(vector<vector<int>>&m){vector<int> r;if(m.empty())return r;int t=0,b=m.size()-1,l=0,rg=m[0].size()-1;while(t<=b&&l<=rg){for(int j=l;j<=rg;j++)r.push_back(m[t][j]);t++;for(int i=t;i<=b;i++)r.push_back(m[i][rg]);rg--;if(t<=b){for(int j=rg;j>=l;j--)r.push_back(m[b][j]);b--;}if(l<=rg){for(int i=b;i>=t;i--)r.push_back(m[i][l]);l++;}}return r;}
int main(){vector<vector<int>> m={{1,2,3},{4,5,6},{7,8,9}};auto r=spiral(m);for(int x:r)cout<<x<<" ";cout<<"\n";}
