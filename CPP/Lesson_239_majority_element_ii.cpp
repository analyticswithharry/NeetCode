// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 239 -- Majority Element II
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 120
// =============================================================
//
// QUESTION:
//   All elements appearing more than n/3 times. Boyer-Moore variant.
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
vector<int> majorityIII(vector<int> nums){int c1=0,c2=0,n1=0,n2=1;for(int x:nums){if(x==n1)c1++;else if(x==n2)c2++;else if(c1==0){n1=x;c1=1;}else if(c2==0){n2=x;c2=1;}else{c1--;c2--;}}vector<int> r;for(int n:{n1,n2}){int cnt=count(nums.begin(),nums.end(),n);if(cnt>(int)nums.size()/3&&find(r.begin(),r.end(),n)==r.end())r.push_back(n);}return r;}
int main(){for(int x:majorityIII({1,1,1,3,3,2,2,2}))cout<<x<<" ";cout<<"\n";}
