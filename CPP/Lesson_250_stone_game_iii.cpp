// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 250 -- Stone Game III
// Category   : 1-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 125
// =============================================================
//
// QUESTION:
//   Players take 1-3 stones from front; maximize own score. Return Alice/Bob/Tie.
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
string stoneGameIII(vector<int> s){int n=s.size();vector<int> dp(n+1,0);for(int i=n-1;i>=0;i--){int best=INT_MIN,take=0;for(int k=0;k<3&&i+k<n;k++){take+=s[i+k];best=max(best,take-dp[i+k+1]);}dp[i]=best;}if(dp[0]>0)return "Alice";if(dp[0]<0)return "Bob";return "Tie";}
int main(){cout<<stoneGameIII({1,2,3,7})<<"\n";}
