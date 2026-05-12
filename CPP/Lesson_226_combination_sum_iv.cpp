// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 226 -- Combination Sum IV
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 113
// =============================================================
//
// QUESTION:
//   Count ordered combinations of nums summing to target.
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
int combSum4(vector<int> nums,int t){vector<unsigned long long> dp(t+1,0);dp[0]=1;for(int v=1;v<=t;v++)for(int x:nums)if(v>=x)dp[v]+=dp[v-x];return (int)dp[t];}
int main(){cout<<combSum4({1,2,3},4)<<"\n";}
