// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 224 -- Regular Expression Matching
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 112
// =============================================================
//
// QUESTION:
//   Implement regex with '.' and '*' (zero or more of preceding).
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
bool isMatch(string s,string p){int m=s.size(),n=p.size();vector<vector<bool>> dp(m+1,vector<bool>(n+1,false));dp[0][0]=true;for(int j=1;j<=n;j++)if(p[j-1]=='*')dp[0][j]=dp[0][j-2];for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){if(p[j-1]=='.'||p[j-1]==s[i-1])dp[i][j]=dp[i-1][j-1];else if(p[j-1]=='*')dp[i][j]=dp[i][j-2]||((p[j-2]=='.'||p[j-2]==s[i-1])&&dp[i-1][j]);}return dp[m][n];}
int main(){cout<<isMatch("aa","a*")<<"\n";}
