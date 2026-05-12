// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 147 -- Last Stone Weight II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 74
// =============================================================
//
// QUESTION:
//   Given stones, smash to minimize remaining weight (subset partition).
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
int lsw2(vector<int> s){int t=accumulate(s.begin(),s.end(),0);int cap=t/2;vector<int> dp(cap+1,0);dp[0]=1;for(int x:s)for(int j=cap;j>=x;j--)dp[j]=dp[j]||dp[j-x];for(int j=cap;j>=0;j--)if(dp[j])return t-2*j;return 0;}
int main(){cout<<lsw2({2,7,4,1,8,1})<<"\n"<<lsw2({31,26,33,21,40})<<"\n";}
