// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 230 -- Integer Break
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 115
// =============================================================
//
// QUESTION:
//   Break n into >=2 positive ints; maximize product.
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
int integerBreak(int n){vector<int> dp(n+1);dp[1]=1;for(int i=2;i<=n;i++)for(int j=1;j<i;j++)dp[i]=max(dp[i],j*max(i-j,dp[i-j]));return dp[n];}
int main(){cout<<integerBreak(10)<<"\n";}
