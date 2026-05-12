// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 223 -- Burst Balloons
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 112
// =============================================================
//
// QUESTION:
//   Burst balloons; coins = nums[l]*nums[i]*nums[r]. Maximize total.
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
int maxCoins(vector<int> nums){vector<int> a;a.push_back(1);for(int x:nums)a.push_back(x);a.push_back(1);int n=a.size();vector<vector<int>> dp(n,vector<int>(n,0));for(int L=2;L<n;L++)for(int l=0;l+L<n;l++){int r=l+L;for(int i=l+1;i<r;i++)dp[l][r]=max(dp[l][r],dp[l][i]+dp[i][r]+a[l]*a[i]*a[r]);}return dp[0][n-1];}
int main(){cout<<maxCoins({3,1,5,8})<<"\n";}
