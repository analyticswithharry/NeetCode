// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 214 -- Minimum Size Subarray Sum
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 107
// =============================================================
//
// QUESTION:
//   Return the minimum length of a contiguous subarray whose sum is >= target. 0 if none.
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
int minSubArrayLen(int t,vector<int> n){int l=0,s=0,ans=INT_MAX;for(int r=0;r<(int)n.size();r++){s+=n[r];while(s>=t){ans=min(ans,r-l+1);s-=n[l++];}}return ans==INT_MAX?0:ans;}
int main(){cout<<minSubArrayLen(7,{2,3,1,2,4,3})<<"\n";}
