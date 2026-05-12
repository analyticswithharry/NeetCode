// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 215 -- Merge Triplets to Form Target Triplet
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 108
// =============================================================
//
// QUESTION:
//   Pick triplets where every value <= target; check if max across them equals target.
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
bool mergeTriplets(vector<vector<int>> t,vector<int> T){vector<int> g(3);for(auto&x:t)if(x[0]<=T[0]&&x[1]<=T[1]&&x[2]<=T[2])for(int i=0;i<3;i++)g[i]=max(g[i],x[i]);return g==T;}
int main(){cout<<mergeTriplets({{2,5,3},{1,8,4},{1,7,5}},{2,7,5})<<"\n";}
