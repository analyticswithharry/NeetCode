// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 225 -- Partition Equal Subset Sum
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 113
// =============================================================
//
// QUESTION:
//   Can the array be split into two equal-sum subsets? Subset-sum DP.
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
bool canPartition(vector<int> nums){int s=accumulate(nums.begin(),nums.end(),0);if(s&1)return false;int t=s/2;vector<bool> dp(t+1,false);dp[0]=true;for(int x:nums)for(int v=t;v>=x;v--)dp[v]=dp[v]||dp[v-x];return dp[t];}
int main(){cout<<canPartition({1,5,11,5})<<"\n";}
