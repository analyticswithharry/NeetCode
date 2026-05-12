// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 229 -- Perfect Squares
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 115
// =============================================================
//
// QUESTION:
//   Min number of perfect-square numbers summing to n.
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
int numSquares(int n){vector<int> dp(n+1,INT_MAX);dp[0]=0;for(int i=1;i<=n;i++)for(int j=1;j*j<=i;j++)dp[i]=min(dp[i],dp[i-j*j]+1);return dp[n];}
int main(){cout<<numSquares(12)<<"\n";}
