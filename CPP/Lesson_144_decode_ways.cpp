// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 144 -- Decode Ways
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 72
// =============================================================
//
// QUESTION:
//   Number of ways to decode digit string s where '1'->A, ..., '26'->Z.
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
int ways(string s){if(s.empty()||s[0]=='0')return 0;int n=s.size();vector<int> dp(n+1,0);dp[0]=1;dp[1]=1;for(int i=2;i<=n;i++){if(s[i-1]!='0')dp[i]+=dp[i-1];int x=stoi(s.substr(i-2,2));if(x>=10&&x<=26)dp[i]+=dp[i-2];}return dp[n];}
int main(){cout<<ways("12")<<"\n"<<ways("226")<<"\n"<<ways("06")<<"\n";}
