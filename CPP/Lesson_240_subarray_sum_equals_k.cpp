// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 240 -- Subarray Sum Equals K
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 120
// =============================================================
//
// QUESTION:
//   Count subarrays with sum k using prefix-sum frequency map.
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
int subarraySum(vector<int> n,int k){unordered_map<int,int> m;m[0]=1;int s=0,c=0;for(int x:n){s+=x;c+=m[s-k];m[s]++;}return c;}
int main(){cout<<subarraySum({1,1,1},2)<<"\n";}
